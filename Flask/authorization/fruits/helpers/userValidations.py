from flask import abort
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
roles = ("admin", "user")


def validate_login_data(data):
    if not data:
        abort(400, "No hay datos del usuario")

    user_name = data.get("userName")
    password = data.get("password")

    if not user_name:
        abort(400, "El nombre de usuario es obligatorio")

    if not password:
        abort(400, "El password es obligatorio")


def validate_user_data(data):
    if not data:
        abort(400, "No hay datos del usuario")

    name = data.get("name")
    email = data.get("email")
    role = data.get("role")

    if not name:
        abort(400, "El nombre es obligatorio")

    if not role:
        abort(400, "El rol es obligatorio")

    if role.lower() not in roles:
        abort(400, "Rol invalido")

    if not email:
        abort(400, "El correo es obligatorio")

    if not EMAIL_REGEX.match(email):
        abort(400, "El email no es valido")

    validate_login_data(data)
