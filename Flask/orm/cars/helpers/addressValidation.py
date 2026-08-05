from flask import abort

def validate_address_data(data):
    if not data:
        abort(400, "No hay datos de la dirección")
    
    street = data.get("street")
    city = data.get("city")
    state = data.get("state")
    zip_code = data.get("zipCode")
    user_id = data.get("userId")

    if not street:
        abort(400, "La calle es obligatoria")
    
    if not city:
        abort(400, "La ciudad es obligatoria")
    
    if not state:
        abort(400, "El estado es obligatorio")
    
    if not zip_code:
        abort(400, "El código postal es obligatorio")

    if user_id is None:
        abort(400, "El id del usuario es obligatorio")
