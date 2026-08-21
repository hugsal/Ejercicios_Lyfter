from flask import abort


def validate_product_data(data):
    if not data:
        abort(400, "No se recibieron datos del producto")

    name = data.get("name")
    price = data.get("price")
    stock = data.get("stock")

    if not name or not str(name).strip():
        abort(400, "El nombre del producto es obligatorio")

    if price is None or not isinstance(price, (int, float)) or price < 0:
        abort(400, "El precio es obligatorio y debe ser un número mayor o igual a 0")

    if stock is None or not isinstance(stock, int) or stock < 0:
        abort(400, "El stock es obligatorio y debe ser un número entero mayor o igual a 0")
