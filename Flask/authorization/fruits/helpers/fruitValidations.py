def validate_fruit_data(data):
    if not data:
        abort(400, "No hay datos del la fruta")

    name = data.get("name")
    price = data.get("price")
    admission_date = data.get("admissionDate")
    quantity = data.get("quantity")

    if not name:
        abort(400, "El nombre es obligatorio")

    if not price:
        abort(400, "El precio es obligatorio")

    if not quantity:
        abort(400, "la cantidad es obligatoria")
