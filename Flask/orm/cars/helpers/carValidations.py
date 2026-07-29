from flask import abort

def validate_car_data(data):
    if not data:
        abort(400, "No hay datos del carro")
    
    brand = data.get("brand")
    model = data.get("model")
    year = data.get("year")

    if not brand:
        abort(400, "La marca es obligatoria")
    
    if not model:
        abort(400, "El modelo es obligatorio")
    
    if not year:
        abort(400, "El año es obligatorio")
    