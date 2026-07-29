from flask import Flask, request, abort
from database import engine, BaseDb, SessionLocal
from repositories.userRepository import UserRepository
from repositories.carRepository import CarRepository
from repositories.addressRepository import AddressRepository
from helpers.userValidations import validate_user_data
from helpers.carValidations import validate_car_data
from helpers.addressValidation import validate_address_data

app = Flask(__name__)

with app.app_context():
    BaseDb.metadata.create_all(bind=engine)

def get_db():
    from flask import g
    if 'db' not in g:
        g.db = SessionLocal()
    return g.db

@app.teardown_appcontext
def close_db(exception=None):
    from flask import g
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route("/users", methods=["GET", "POST"])
def create_user():
    if request.method == "GET":
        db = get_db()
        return {"users": UserRepository.get_users(db)}, 200

    if request.method == "POST":
        data = request.json
        validate_user_data(data)
        db = get_db()

        name = data.get("name")
        email = data.get("email")
        user_name = data.get("userName")

        if UserRepository.get_user_by_name(db, user_name):
            abort(400, "El nombre de usuario ya existe")
        
        if UserRepository.get_user_by_email(db, email):
            abort(400, "El correo ya existe")

        new_user = UserRepository.create_user(db, name, email, user_name)
        return {"user": new_user}, 200

    return {}, 405


@app.route("/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def manage_user(user_id):
    db = get_db()
    if request.method == "GET":
        user = UserRepository.get_user_by_id(db, user_id)
        if not user:
            abort(404, "Usuario no encontrado")
        return {"user": user}, 200
    
    if request.method == "PUT":
        data = request.json
        name = data.get("name")
        email = data.get("email")
        user_name = data.get("userName")
        
        user = UserRepository.get_user_by_id(db, user_id)
        if not user:
            abort(404, "Usuario no encontrado")

        if user_name and user["userName"] != user_name and UserRepository.get_user_by_name(db, user_name):
            abort(400, "El nombre de usuario ya existe")
        
        if email and user["email"] != email and UserRepository.get_user_by_email(db, email):
            abort(400, "El correo ya existe")

        user = UserRepository.update_user(db, user_id, name, email, user_name)
        return {"user": user}, 200
    
    if request.method == "DELETE":
        user = UserRepository.get_user_by_id(db, user_id)
        if not user:
            abort(404, "Usuario no encontrado")
        
        UserRepository.delete_user(db, user["id"])
        return {}, 200

    return {}, 405

@app.route("/cars", methods=["GET", "POST"])
def manage_cars():
    if request.method == "GET":
        db = get_db()
        cars = CarRepository.get_cars(db)
        return {"cars": cars}, 200

    if request.method == "POST":
        db = get_db()
        data = request.json
        validate_car_data(data)
        brand = data.get("brand")
        model = data.get("model")
        year = data.get("year")
        user_id = data.get("userId", None)

        if user_id is not None and not UserRepository.get_user_by_id(db, user_id):
            abort(404, "Usuario no encontrado")

        new_car = CarRepository.create_car(db, brand, model, year, user_id)
        return {"car": new_car}, 200

    return {}, 405

@app.route("/cars/<car_id>", methods=["GET", "PUT", "DELETE"])
def manage_car(car_id):
    db = get_db()
    if request.method == "GET":
        car = CarRepository.get_car_by_id(db, car_id)
        return {"car": car}, 200
    
    if request.method == "PUT":
        data = request.json
        validate_car_data(data)
        brand = data.get("brand")
        model = data.get("model")
        year = data.get("year")
        user_id = data.get("userId", None)

        if not CarRepository.get_car_by_id(db, car_id):
            abort(404, "Carro no encontrado")

        if user_id and not UserRepository.get_user_by_id(db, user_id):
            abort(404, "Usuario no encontrado")

        car = CarRepository.update_car(db, car_id, brand, model, year, user_id)
        return {"car": car}, 200
    
    if request.method == "DELETE":
        car = CarRepository.get_car_by_id(db, car_id)
        if not car:
            abort(404, "Carro no encontrado")
        
        CarRepository.delete_car(db, car["id"])
        return {}, 200

    return {}, 405

@app.route("/address", methods=["GET", "POST"])
def manage_addresses():
    if request.method == "GET":
        db = get_db()
        addresses = AddressRepository.get_addresses(db)
        return {"addresses": addresses}, 200

    if request.method == "POST":
        db = get_db()
        data = request.json
        validate_address_data(data)
        street = data.get("street")
        city = data.get("city")
        state = data.get("state")
        zip_code = data.get("zipCode")
        user_id = data.get("userId")

        if not UserRepository.get_user_by_id(db, user_id):
            abort(404, "Usuario no encontrado")

        new_address = AddressRepository.create_address(db, street, city, state, zip_code, user_id)
        return {"address": new_address}, 200

    return {}, 405

@app.route("/address/<address_id>", methods=["GET", "PUT", "DELETE"])
def manage_address(address_id):
    db = get_db()
    if request.method == "GET":
        address = AddressRepository.get_address_by_id(db, address_id)
        if not address:
            abort(404, "Dirección no encontrada")
        return {"address": address}, 200
    
    if request.method == "PUT":
        data = request.json
        validate_address_data(data)
        street = data.get("street")
        city = data.get("city")
        state = data.get("state")
        zip_code = data.get("zipCode")
        user_id = data.get("userId")

        if not AddressRepository.get_address_by_id(db, address_id):
            abort(404, "Dirección no encontrada")

        if not UserRepository.get_user_by_id(db, user_id):
            abort(404, "Usuario no encontrado")

        address = AddressRepository.update_address(db, address_id, street, city, state, zip_code, user_id)
        return {"address": address}, 200
    
    if request.method == "DELETE":
        address = AddressRepository.get_address_by_id(db, address_id)
        if not address:
            abort(404, "Dirección no encontrada")
        
        AddressRepository.delete_address(db, address["id"])
        return {}, 200

    return {}, 405

@app.route("/user/<user_id>/car/<car_id>", methods=["PUT"])
def assign_car_to_user(user_id, car_id):
    db = get_db()
    user = UserRepository.get_user_by_id(db, user_id)
    car = CarRepository.get_car_by_id(db, car_id)
    if not user or not car:
        abort(404, "Usuario o carro no encontrado")
    car_updated = CarRepository.update_car(db, car["id"], car["brand"], car["model"], car["year"], user["id"])
    return {"car": car_updated}, 200

if __name__ == "__main__":
    app.run(host="localhost", port=4000, debug=True)