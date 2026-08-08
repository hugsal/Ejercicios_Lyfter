from validations import validate_car


class CarService:
    def __init__(self, car_repository):
        self.car_repository = car_repository

    def get_all_cars(self, params):
        return self.car_repository.get_all_cars(params)

    def get_car_by_id(self, car_id):
        return self.car_repository.get_car_by_id(car_id)

    def create_car(self, data):
        validate_car(data)
        make = data.get("make", None)
        model = data.get("model", None)
        car_year = data.get("year", None)

        return self.car_repository.create_car(make, model, car_year)

    def change_car_status(self, new_status, car_id):
        return self.car_repository.change_car_status(new_status, car_id)
