from flask import Flask, request, abort
from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST
from userService import UserService
from userRepository import UserRepository
from carService import CarService
from carRepository import CarRepository
from rentalService import RentalService
from rentalRepository import RentalRepository
from validations import validate_user_params, validate_car_params

app = Flask(__name__)
db_manager = DbManager(DB_NAME, USER, PASSWORD, HOST)
user_repository = UserRepository(db_manager)
user_service = UserService(user_repository)
car_repository = CarRepository(db_manager)
car_service = CarService(car_repository)
rental_repository = RentalRepository(db_manager)
rental_service = RentalService(rental_repository)


@app.route("/users", methods=["GET", "POST"])
def user():
    method = request.method

    if method == "GET":
        params = request.args
        if params:
            validate_user_params(params)

        users = user_service.get_all_users(params)
        if not users:
            abort(404, "No users found")

        return {"users": users}, 200

    if method == "POST":
        data = request.json
        user = user_service.create_user(data)
        return {"user": user}, 200

    return {}, 403


@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    method = request.method
    if method == "PUT":
        data = request.json
        user = user_service.get_user_by_id(id)
        if not user:
            abort(404, "User not found")
        usre = user_service.update_user(user["id"], data)
        return {"user": user}, 200

    return {}, 403


@app.route("/cars", methods=["GET", "POST"])
def car():
    method = request.method

    if method == "GET":
        params = request.args
        if params:
            validate_car_params(params)

        cars = car_service.get_all_cars(params)
        if not cars:
            abort(404, "No cars found")

        return {"cars": cars}, 200

    if method == "POST":
        data = request.json
        car = car_service.create_car(data)
        return {"car": car}, 200

    return {}, 403


@app.route("/rental", methods=["GET", "POST"])
def rental():
    method = request.method

    if method == "GET":
        params = request.args
        if params:
            validate_rental_params(params)

        rentals = rental_service.get_all_rentals(params)
        if not rentals:
            abort(404, "No rentals found")

        return {"rentals": rentals}, 200

    if method == "POST":
        data = request.json
        user = user_service.get_user_by_id(data["userId"])
        car = car_service.get_car_by_id(data["carId"])
        if not user or not car:
            abort(404, "User or car not found")

        if car["status"] == "rented":
            abort(400, "Car is not active")

        rental = rental_service.create_rental(user["id"], car["id"])
        car_service.change_car_status("rented", car["id"])

        return {"rental": rental}, 200


if __name__ == "__main__":
    app.run(host="localhost", port=4000, debug=True)
