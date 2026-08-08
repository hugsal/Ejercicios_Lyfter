from flask import abort
from datetime import datetime
import re


def validate_type(value, field):
    if isinstance(value, str):
        clean_value = value.strip()
        if not clean_value:
            abort(400, f"El campo {field} no puede estar vacío.")
    else:
        abort(400, f"El campo {field} debe ser texto.")


def validate_email(email):
    PATRON_EMAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(PATRON_EMAIL, email):
        return True

    abort(400, "El email no es valido")


def validate_date(date):
    try:
        date_val = datetime.strptime(date, "%d/%m/%Y").date()
    except (ValueError, TypeError) as ex:
        abort(400, "la fecha debe ser en formato dd/mm/yyyy")


def validate_user(user_json):
    if not user_json:
        abort(400, "No hay datos del usuario")

    name = user_json.get("name", None)
    email = user_json.get("email", None)
    username = user_json.get("userName", None)
    password = user_json.get("password", None)
    bornDate = user_json.get("bornDate", None)

    if not name:
        abort(400, "El nombre es obligatorio")
    validate_type(name, "nombre")

    if not email:
        abort(400, "El email es obligatorio")
    validate_email(email)

    if not username:
        abort(400, "El username es obligatorio")
    validate_type(username, "username")

    if not password:
        abort(400, "El password es obligatorio")
    validate_type(password, "password")

    if not bornDate:
        abort(400, "La fecha de nacimiento es obligatoria")
    validate_date(bornDate)


def validate_car(car_json):
    if not car_json:
        abort(400, "No hay datos del vehiculo")
    make = car_json.get("make", None)
    model = car_json.get("model", None)
    car_year = car_json.get("year", None)

    if not make:
        abort(400, "La marca es obligatoria")
    validate_type(make, "marca")

    if not model:
        abort(400, "El modelo es obligatorio")
    validate_type(model, "modelo")

    if not car_year:
        abort(400, "El año es obligatorio")

    if not isinstance(car_year, int):
        abort(400, "El año debe ser un numero")


def validate_user_params(params):
    ALLOWED_COLUMNS = {
        "full_name",
        "email",
        "user_name",
        "born_date",
        "account_status",
    }
    key = list(params.items())[0][0]
    if key not in ALLOWED_COLUMNS:
        abort(400, "Invalid column")


def validate_car_params(params):
    ALLOWED_COLUMNS = {
        "make",
        "model",
        "year",
        "status",
    }
    key = list(params.items())[0][0]
    if key not in ALLOWED_COLUMNS:
        abort(400, "Invalid column")


def validate_rental_params(params):
    ALLOWED_COLUMNS = {
        "rent_date",
        "rental_status",
    }
    key = list(params.items())[0][0]
    if key not in ALLOWED_COLUMNS:
        abort(400, "Invalid column")
