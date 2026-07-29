from flask import abort
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def validate_user_data(data):
    if not data:
        abort(400, "No hay datos del usuario")
    
    name = data.get("name")
    email = data.get("email")
    user_name = data.get("userName")

    if not name:
        abort(400, "El nombre es obligatorio")
    
    if not email:
        abort(400, "El correo es obligatorio")

    if not user_name:
        abort(400, "El nombre de usuario es obligatorio")

    if not EMAIL_REGEX.match(email):
        abort(400, "El email no es valido")