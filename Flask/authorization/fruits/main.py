from flask import Flask, request, abort
from database import engine, BaseDb, SessionLocal
from repositories.userRepository import UserRepository
from repositories.fruitRepository import FruitRepository
from repositories.invoiceRepository import InvoiceRepository
from repositories.fruitInvoiceRepository import FruitsInvoiceRepository
from helpers.userValidations import validate_user_data, validate_login_data
from helpers.fruitValidations import validate_fruit_data
from validateRoles import validate_roles
from extension import jwt_manager, cache_manager
import json

app = Flask(__name__)

with app.app_context():
    BaseDb.metadata.create_all(bind=engine)


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


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    validate_login_data(data)
    db = get_db()

    user_name = data.get("userName")
    user = UserRepository.get_user_by_user_name(db, user_name)
    if not user:
        abort(401, "Usuario o Password incorrecto")

    if data.get("password") != user.get("password"):
        abort(401, "Usuario o Password incorrecto")

    user_id = user.get("id")
    rol = user.get("role")
    token = jwt_manager.encode({"id": user_id, "role": rol})

    return {"token": token}, 200


@app.route("/me")
@validate_roles(["admin", "user"])
def me():
    db = get_db()
    authenticated_user = request.user_payload
    user_id = authenticated_user["id"]
    user = UserRepository.get_user_by_id(db, user_id)
    return {"userId": user_id, "userName": user["userName"]}, 200


@app.route("/users")
@validate_roles(["admin"])
def get_users():
    db = get_db()
    return {"users": UserRepository.get_users(db)}, 200


@app.route("/users", methods=["POST"])
@validate_roles(["admin"])
def crete_user():
    data = request.json
    validate_user_data(data)
    db = get_db()

    name = data.get("name")
    email = data.get("email")
    role = data.get("role").lower()
    user_name = data.get("userName")
    password = data.get("password")

    if UserRepository.get_user_by_user_name(db, user_name):
        abort(400, "El nombre de usuario ya existe")

    if UserRepository.get_user_by_email(db, email):
        abort(400, "El correo ya existe")

    new_user = UserRepository.create_user(db, name, email, role, user_name, password)
    return {"user": new_user}, 201


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
    data = request.json
    validate_user_data(data)
    db = get_db()

    user = UserRepository.get_user_by_id(db, user_id)
    if not user:
        abort(404, "Usuario no encontrado")

    data = request.json
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

    user = UserRepository.update_user(db, user_id, name, email, user_name, role)
    return {"user": user}, 200


@app.route("/users/<user_id>", methods=["DELETE"])
@validate_roles(["admin"])
def delete_user(user_id):
    db = get_db()
    user = UserRepository.get_user_by_id(db, user_id)
    if not user:
        abort(404, "Usuario no encontrado")

    UserRepository.delete_user(db, user["id"])
    return {}, 200


@app.route("/fruits")
@validate_roles(["admin"])
def get_fruits():
    db = get_db()
    cache_fruit_ids = cache_manager.get_list_data("fruits:id")

    if not cache_fruit_ids:
        fruits = FruitRepository.get_fruits(db)
        if not fruits:
            return {"fruits": fruits}, 200
        try:
            fruit_ids = [fruit["id"] for fruit in fruits]
            cache_manager.store_list("fruits:id", fruit_ids)
            for fruit in fruits:
                cache_manager.store_data(f"fruit:{fruit["id"]}", json.dumps(fruit))
        except:
            abort(500, " Error al procesar datos de cache")

        return {"fruits": fruits}, 200

    fruit_ids = [f"fruit:{fruit_id}" for fruit_id in cache_fruit_ids]
    fruits = [
        json.loads(fruit) if fruit else None
        for fruit in cache_manager.get_all_data(fruit_ids)
    ]
    result = []
    missing_ids = []

    for index, value in enumerate(fruits):
        if value is None:
            missing_ids.append(fruit_ids[index].split(":")[1])
        else:
            result.append(value)

    if missing_ids:
        missing_fruits = FruitRepository.get_fruit_by_ids(db, missing_ids)

        for fruit in missing_fruits:
            cache_manager.store_data(f"fruit:{fruit["id"]}", json.dumps(fruit))
            result.append(fruit)

    return {"fruits": result}, 200


@app.route("/fruits", methods=["POST"])
@validate_roles(["admin"])
def create_fruit():
    data = request.json
    validate_fruit_data(data)
    db = get_db()

    name = data.get("name")
    price = data.get("price")
    quantity = data.get("quantity")

    if FruitRepository.get_fruit_by_name(db, name):
        abort(400, "La fruta ya existe")

    cache_fruit_ids = cache_manager.get_list_data("fruits:id")
    if not cache_fruit_ids:
        fruits = FruitRepository.get_fruits(db)
        if fruits:
            try:
                fruit_ids = [fruit["id"] for fruit in fruits]
                cache_manager.store_list("fruits:id", fruit_ids)
                for fruit in fruits:
                    cache_manager.store_data(f"fruit:{fruit["id"]}", json.dumps(fruit))
            except:
                abort(500, " Error al procesar datos de cache")

    new_fruit = FruitRepository.create_fruit(db, name, price, quantity)
    cache_manager.store_list("fruits:id", [new_fruit["id"]])
    cache_manager.store_data(f"fruit:{new_fruit["id"]}", json.dumps(new_fruit))

    return {"fruit": new_fruit}, 201


@app.route("/fruits/<fruit_id>")
@validate_roles(["admin"])
def get_fruit_by_id(fruit_id):
    db = get_db()
    fruit = cache_manager.get_data(f"fruit:{fruit_id}")
    if fruit:
        return {"fruit": json.loads(fruit)}, 200

    fruit = FruitRepository.get_fruit_by_id(db, fruit_id)
    if not fruit:
        abort(404, "Fruta no encontrada")

    cache_manager.store_data(f"fruit:{fruit_id}", json.dumps(fruit))
    return {"fruit": fruit}, 200


@app.route("/fruits/<fruit_id>", methods=["PUT"])
@validate_roles(["admin"])
def update_fruit(fruit_id):
    data = request.json
    validate_fruit_data(data)
    db = get_db()

    fruit = FruitRepository.get_fruit_by_id(db, fruit_id)
    if not fruit:
        abort(404, "Fruta no encontrada")

    name = data.get("name")
    price = data.get("price")
    quantity = data.get("quantity")

    updated_fruit = FruitRepository.update_fruit(db, fruit["id"], name, price, quantity)
    cache_manager.delete_data(f"fruit:{fruit_id}")

    return {"fruit": updated_fruit}, 200


@app.route("/fruits/<fruit_id>", methods=["DELETE"])
@validate_roles(["admin"])
def delete_fruit(fruit_id):
    db = get_db()
    fruit = FruitRepository.get_fruit_by_id(db, fruit_id)
    if not fruit:
        abort(404, "Fruta no encontrado")

    FruitRepository.delete_fruit(db, fruit["id"])
    cache_manager.delete_data(f"fruit:{fruit_id}")
    cache_manager.delete_from_list("fruits:id", fruit_id)
    return {}, 200


@app.route("/sales", methods=["POST"])
@validate_roles(["admin", "user"])
def sales():
    data = request.json
    db = get_db()
    authenticated_user = request.user_payload
    user_id = authenticated_user["id"]

    if not user_id or not UserRepository.get_user_by_id(db, user_id):
        abort(400, "El usuario no es valido")

    fruits = data.get("fruits")
    if not fruits:
        abort(400, "No hay informacion para procesar")

    available_fruits = []

    for fruit in fruits:
        available_fruit = FruitRepository.get_fruit_by_id(db, fruit["fruitId"])
        if available_fruit and available_fruit["quantity"] >= fruit["quantity"]:
            available_fruits.append(available_fruit)
            continue
        abort(400, f"No se puede procesar la fruta con id: {fruit["fruitId"]}")

    invoice = InvoiceRepository.create_invoice(db, user_id, total_amount=0)
    total_amount = 0

    for index in range(len(available_fruits)):
        fruit_id = available_fruits[index]["id"]
        quantity = fruits[index]["quantity"]
        price = available_fruits[index]["price"]
        partial_amount = price * quantity
        total_amount += partial_amount
        FruitsInvoiceRepository.create_register(
            db, quantity, partial_amount, fruit_id, invoice["id"]
        )
        FruitRepository.subtract_from_inventory(db, fruit_id, quantity)
        cache_manager.delete_data(f"fruit:{fruit_id}")

    invoice = InvoiceRepository.update_total_amount(db, invoice["id"], total_amount)

    return {"invoice": invoice}, 201


@app.route("/invoices")
@validate_roles(["admin", "user"])
def get_invoices():
    payload = request.user_payload
    user_id = payload["id"]
    db = get_db()
    user_id_int = int(user_id)
    return {"invoices": InvoiceRepository.get_invoice_by_user_id(db, user_id_int)}, 200


if __name__ == "__main__":
    app.run(host="localhost", port=4000, debug=True)
