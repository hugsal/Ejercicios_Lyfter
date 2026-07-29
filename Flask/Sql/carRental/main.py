from flask import Flask, request, abort
from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST
from userService import UserService
from userRepository import UserRepository
from carService import CarService
from carRepository import CarRepository
from rentalService import RentalService
from rentalRepository import RentalRepository
from validations import (
    validate_user_params,
    validate_car_params,
    validate_rental_params,
)

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
        updated_user = user_service.update_user(user["id"], data)
        return {"user": updated_user}, 200

    return {}, 403


@app.route("/users/<id>/defaulter", methods=["PUT"])
def flag_user_defaulter(id):
    user = user_service.get_user_by_id(id)
    if not user:
        abort(404, "User not found")
    updated_user = user_service.flag_defaulter(user["id"])
    return {"user": updated_user}, 200


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


@app.route("/cars/<id>", methods=["PUT"])
def update_car(id):
    data = request.json
    status = data.get("status")
    if not status:
        abort(400, "status is required")
    car = car_service.get_car_by_id(id)
    if not car:
        abort(404, "Car not found")
    updated_car = car_service.change_car_status(status, car["id"])
    return {"car": updated_car}, 200


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
        user_id = data.get("userId")
        car_id = data.get("carId")
        if not user_id or not car_id:
            abort(400, "userId and carId are required")

        user = user_service.get_user_by_id(user_id)
        car = car_service.get_car_by_id(car_id)
        if not user or not car:
            abort(404, "User or car not found")

        if car["status"] != "ready":
            abort(400, "Car is not available for rent")

        rental = rental_service.create_rental(user["id"], car["id"])
        car_service.change_car_status("rented", car["id"])

        return {"rental": rental}, 200


@app.route("/rental/<id>", methods=["PUT"])
def update_rental(id):
    data = request.json
    status = data.get("status")
    if not status:
        abort(400, "status is required")
    rental = rental_service.get_rental_by_id(id)
    if not rental:
        abort(404, "Rental not found")
    updated_rental = rental_service.update_rental_status(id, status)
    return {"rental": updated_rental}, 200


@app.route("/rental/<id>/finish", methods=["PUT"])
def finish_rental(id):
    rental = rental_service.get_rental_by_id(id)
    if not rental:
        abort(404, "Rental not found")
    updated_rental = rental_service.finish_rental(id)
    return {"rental": updated_rental}, 200


if __name__ == "__main__":
    app.run(host="localhost", port=4000, debug=True)
