from datetime import datetime, timedelta, timezone
from flask import Flask, request, abort
from werkzeug.exceptions import HTTPException

from database import engine, BaseDb, SessionLocal
from entities.userEntity import User
from entities.productEntity import Product
from entities.cartEntity import Cart, CartItem
from entities.invoiceEntity import Invoice
from entities.invoiceItemEntity import InvoiceItem

from repositories.userRepository import UserRepository
from repositories.productRepository import ProductRepository
from repositories.cartRepository import CartRepository
from repositories.invoiceRepository import InvoiceRepository
from repositories.invoiceItemRepository import InvoiceItemRepository

from helpers.userValidations import validate_user_data, validate_login_data
from helpers.productValidations import validate_product_data
from helpers.salesValidations import validate_checkout_data

from validateRoles import validate_roles
from extension import jwt_manager
from cacheManager import cache_manager

app = Flask(__name__)

with app.app_context():
    BaseDb.metadata.create_all(bind=engine)


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Manejador global para retornar errores HTTP en formato JSON."""
    return {"message": e.description}, e.code


def get_db():
    from flask import g

    if "db" not in g:
        g.db = SessionLocal()
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    from flask import g

    db = g.pop("db", None)
    if db is not None:
        db.close()


def generate_tokens(user_id, role):
    now = datetime.now(timezone.utc)
    exp_access = now + timedelta(minutes=15)
    access_token = jwt_manager.encode(
        {"id": user_id, "role": role, "exp": int(exp_access.timestamp())}
    )
    exp_refresh = now + timedelta(days=15)
    refresh_token = jwt_manager.encode(
        {"id": user_id, "role": role, "exp": int(exp_refresh.timestamp())}
    )
    return access_token, refresh_token


# ==========================================================
# 🔐 MÓDULO DE USUARIOS Y AUTENTICACIÓN
# ==========================================================


@app.route("/sigin", methods=["POST"])
def sigin():
    """Registro de nuevos usuarios / clientes. Retorna usuario y tokens JWT."""
    data = request.json or {}
    validate_user_data(data)
    db = get_db()

    name = data.get("name")
    email = data.get("email")
    role = data.get("role", "client").lower()
    user_name = data.get("userName")
    password = data.get("password")

    if UserRepository.get_user_by_user_name(db, user_name):
        abort(400, "El nombre de usuario ya existe")

    if UserRepository.get_user_by_email(db, email):
        abort(400, "El correo ya existe")

    new_user = UserRepository.create_user(db, name, email, role, user_name, password)
    access_token, refresh_token = generate_tokens(new_user["id"], new_user["role"])

    return {
        "user": new_user,
        "access_token": access_token,
        "refresh_token": refresh_token,
    }, 201


@app.route("/login", methods=["POST"])
def login():
    """Inicio de sesión de usuarios."""
    data = request.json or {}
    validate_login_data(data)
    db = get_db()

    user_name = data.get("userName")
    user = UserRepository.get_user_by_user_name(db, user_name)
    if not user or data.get("password") != user.get("password"):
        abort(401, "Usuario o Password incorrecto")

    access_token, refresh_token = generate_tokens(user["id"], user["role"])
    return {"access_token": access_token, "refresh_token": refresh_token}, 200


@app.route("/me")
@validate_roles(["admin", "client"])
def me():
    """Información del usuario autenticado."""
    db = get_db()
    authenticated_user = request.user_payload
    user_id = authenticated_user["id"]
    user = UserRepository.get_user_by_id(db, user_id)
    if not user:
        abort(404, "Usuario no encontrado")
    return {"user": user}, 200


@app.route("/users")
@validate_roles(["admin"])
def get_users():
    db = get_db()
    return {"users": UserRepository.get_users(db)}, 200


@app.route("/users/<user_id>")
@validate_roles(["admin"])
def get_user_by_id(user_id):
    db = get_db()
    user = UserRepository.get_user_by_id(db, user_id)
    if not user:
        abort(404, "Usuario no encontrado")
    return {"user": user}, 200


@app.route("/users/<user_id>", methods=["PUT"])
@validate_roles(["admin"])
def update_user(user_id):
    data = request.json or {}
    validate_user_data(data)
    db = get_db()

    user = UserRepository.get_user_by_id(db, user_id)
    if not user:
        abort(404, "Usuario no encontrado")

    name = data.get("name")
    email = data.get("email")
    user_name = data.get("userName")
    role = data.get("role")

    if (
        user_name
        and user["userName"] != user_name
        and UserRepository.get_user_by_user_name(db, user_name)
    ):
        abort(400, "El nombre de usuario ya existe")

    if email and user["email"] != email and UserRepository.get_user_by_email(db, email):
        abort(400, "El correo ya existe")

    updated_user = UserRepository.update_user(db, user_id, name, email, user_name, role)
    return {"user": updated_user}, 200


@app.route("/users/<user_id>", methods=["DELETE"])
@validate_roles(["admin"])
def delete_user(user_id):
    db = get_db()
    user = UserRepository.get_user_by_id(db, user_id)
    if not user:
        abort(404, "Usuario no encontrado")

    UserRepository.delete_user(db, user["id"])
    return {}, 200


# ==========================================================
# 🏷️ MÓDULO DE PRODUCTOS (CON CACHEO Y TTL 300s)
# ==========================================================


@app.route("/products")
@validate_roles(["admin", "client"])
def get_products():
    cache_key = "products:all"
    cached_products = cache_manager.get(cache_key)
    if cached_products is not None:
        return {"products": cached_products, "cached": True}, 200

    db = get_db()
    products = ProductRepository.get_products(db)
    cache_manager.set(cache_key, products, ttl=300)
    return {"products": products, "cached": False}, 200


@app.route("/products/<product_id>")
@validate_roles(["admin", "client"])
def get_product_by_id(product_id):
    cache_key = f"products:{product_id}"
    cached_product = cache_manager.get(cache_key)
    if cached_product is not None:
        return {"product": cached_product, "cached": True}, 200

    db = get_db()
    product = ProductRepository.get_product_by_id(db, product_id)
    if not product:
        abort(404, "Producto no encontrado")

    cache_manager.set(cache_key, product, ttl=300)
    return {"product": product, "cached": False}, 200


@app.route("/products", methods=["POST"])
@validate_roles(["admin"])
def create_product():
    data = request.json or {}
    validate_product_data(data)
    db = get_db()

    name = data.get("name")
    price = float(data.get("price"))
    stock = int(data.get("stock"))
    description = data.get("description")

    if ProductRepository.get_product_by_name(db, name):
        abort(400, "El producto ya existe")

    new_product = ProductRepository.create_product(
        db, name, price, stock, description
    )

    cache_manager.invalidate_products()
    return {"product": new_product}, 201


@app.route("/products/<product_id>", methods=["PUT"])
@validate_roles(["admin"])
def update_product(product_id):
    data = request.json or {}
    validate_product_data(data)
    db = get_db()

    product = ProductRepository.get_product_by_id(db, product_id)
    if not product:
        abort(404, "Producto no encontrado")

    name = data.get("name")
    price = float(data.get("price")) if data.get("price") is not None else None
    stock = int(data.get("stock")) if data.get("stock") is not None else None
    description = data.get("description")

    updated_product = ProductRepository.update_product(
        db, product["id"], name, price, stock, description
    )

    cache_manager.invalidate_products()
    return {"product": updated_product}, 200


@app.route("/products/<product_id>", methods=["DELETE"])
@validate_roles(["admin"])
def delete_product(product_id):
    db = get_db()
    product = ProductRepository.get_product_by_id(db, product_id)
    if not product:
        abort(404, "Producto no encontrado")

    ProductRepository.delete_product(db, product["id"])
    cache_manager.invalidate_products()
    return {}, 200


# ==========================================================
# 🛒 MÓDULO DE VENTAS, CARRITOS Y FACTURAS (CON CACHEO Y TTL 600s)
# ==========================================================


@app.route("/carts")
@validate_roles(["admin", "client"])
def get_carts():
    db = get_db()
    user_id = request.user_payload["id"]
    return {"carts": CartRepository.get_user_carts(db, user_id)}, 200


@app.route("/carts/active")
@validate_roles(["admin", "client"])
def get_active_cart():
    db = get_db()
    user_id = request.user_payload["id"]
    cart = CartRepository.get_or_create_active_cart(db, user_id)
    return {"cart": cart}, 200


@app.route("/carts/items", methods=["POST"])
@validate_roles(["admin", "client"])
def add_to_cart():
    data = request.json or {}
    product_id = data.get("productId")
    quantity = data.get("quantity")

    if not product_id:
        abort(400, "El productId es obligatorio")
    if quantity is None or not isinstance(quantity, int):
        abort(400, "La cantidad debe ser un número entero")

    db = get_db()
    user_id = request.user_payload["id"]

    product = ProductRepository.get_product_by_id(db, product_id)
    if not product and quantity > 0:
        abort(404, "El producto especificado no existe")

    active_cart = CartRepository.get_or_create_active_cart(db, user_id)
    updated_cart = CartRepository.add_or_update_item(
        db, active_cart["id"], product_id, quantity
    )
    return {"cart": updated_cart}, 200


@app.route("/carts/items/<product_id>", methods=["DELETE"])
@validate_roles(["admin", "client"])
def remove_from_cart(product_id):
    db = get_db()
    user_id = request.user_payload["id"]
    active_cart = CartRepository.get_or_create_active_cart(db, user_id)
    updated_cart = CartRepository.remove_item(db, active_cart["id"], product_id)
    return {"cart": updated_cart}, 200


@app.route("/sales", methods=["POST"])
@validate_roles(["admin", "client"])
def create_sale():
    data = request.json or {}
    validate_checkout_data(data)
    db = get_db()
    user_id = request.user_payload["id"]

    billing_address = data.get("billingAddress")
    payment_method = data.get("paymentMethod", "SINPE")
    payment_reference = data.get("paymentReference")

    cart_id = data.get("cartId")
    if cart_id:
        cart = CartRepository.get_cart_by_id(db, cart_id)
    else:
        cart = CartRepository.get_or_create_active_cart(db, user_id)

    if not cart or not cart["items"]:
        abort(400, "El carrito de compras está vacío o no es válido")

    items_to_process = []
    for item in cart["items"]:
        product_entity = ProductRepository.get_product_entity_by_id(
            db, item["productId"]
        )
        if not product_entity:
            abort(400, f"Producto id {item['productId']} ya no existe")
        if product_entity.stock < item["quantity"]:
            abort(
                400,
                f"Stock insuficiente para '{product_entity.name}'. Requerido: {item['quantity']}, Disponible: {product_entity.stock}",
            )
        items_to_process.append((product_entity, item["quantity"]))

    invoice = InvoiceRepository.create_invoice(
        db,
        user_id=user_id,
        total_amount=0.0,
        billing_address=billing_address,
        payment_method=payment_method,
        payment_reference=payment_reference,
    )

    total_amount = 0.0
    for product_entity, quantity in items_to_process:
        unit_price = product_entity.price
        subtotal = unit_price * quantity
        total_amount += subtotal

        InvoiceItemRepository.create_register(
            db,
            quantity=quantity,
            unit_price=unit_price,
            subtotal=subtotal,
            product_id=product_entity.id,
            invoice_id=invoice["id"],
        )

        ProductRepository.subtract_stock(db, product_entity.id, quantity)

    updated_invoice = InvoiceRepository.update_total_amount(
        db, invoice["id"], total_amount
    )
    CartRepository.update_cart_status(db, cart["id"], "completed")

    cache_manager.invalidate_products()
    cache_manager.invalidate_invoices()

    return {"invoice": updated_invoice}, 201


@app.route("/invoices")
@validate_roles(["admin", "client"])
def get_invoices():
    db = get_db()
    payload = request.user_payload
    user_id = payload["id"]
    role = str(payload.get("role", "")).lower()

    cache_key = "invoices:admin:all" if role == "admin" else f"invoices:user:{user_id}"
    cached_invoices = cache_manager.get(cache_key)
    if cached_invoices is not None:
        return {"invoices": cached_invoices, "cached": True}, 200

    if role == "admin":
        invoices = InvoiceRepository.get_all_invoices(db)
    else:
        invoices = InvoiceRepository.get_invoices_by_user_id(db, user_id)

    cache_manager.set(cache_key, invoices, ttl=600)
    return {"invoices": invoices, "cached": False}, 200


@app.route("/invoices/<invoice_id>")
@validate_roles(["admin", "client"])
def get_invoice_by_id(invoice_id):
    payload = request.user_payload
    cache_key = f"invoices:detail:{invoice_id}"
    cached_invoice = cache_manager.get(cache_key)

    if cached_invoice is not None:
        if (
            str(payload.get("role")).lower() != "admin"
            and cached_invoice["userId"] != payload["id"]
        ):
            abort(403, "No tienes permisos para ver esta factura")
        return {"invoice": cached_invoice, "cached": True}, 200

    db = get_db()
    invoice = InvoiceRepository.get_invoice_by_id(db, invoice_id)

    if not invoice:
        abort(404, "Factura no encontrada")

    if (
        str(payload.get("role")).lower() != "admin"
        and invoice["userId"] != payload["id"]
    ):
        abort(403, "No tienes permisos para ver esta factura")

    cache_manager.set(cache_key, invoice, ttl=600)
    return {"invoice": invoice, "cached": False}, 200


@app.route("/invoices/<invoice_id>/refund", methods=["POST"])
@validate_roles(["admin", "client"])
def refund_invoice(invoice_id):
    db = get_db()
    payload = request.user_payload
    invoice_entity = InvoiceRepository.get_invoice_entity_by_id(db, invoice_id)

    if not invoice_entity:
        abort(404, "Factura no encontrada")

    if (
        str(payload.get("role")).lower() != "admin"
        and invoice_entity.fk_user_id != payload["id"]
    ):
        abort(403, "No tienes permisos para realizar devoluciones en esta factura")

    if invoice_entity.status == "refunded":
        abort(400, "Esta factura ya ha sido devuelta previamente")

    for item in invoice_entity.items:
        if item.fk_product_id:
            ProductRepository.add_stock(db, item.fk_product_id, item.quantity)

    refunded_invoice = InvoiceRepository.update_status(db, invoice_id, "refunded")

    cache_manager.invalidate_products()
    cache_manager.invalidate_invoices()

    return {"invoice": refunded_invoice}, 200


if __name__ == "__main__":
    app.run(host="localhost", port=4000, debug=True)
