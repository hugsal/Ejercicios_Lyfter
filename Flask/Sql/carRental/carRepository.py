from addCar import add_car
from changeCarStatus import change_car_status


class CarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def __format_car(self, car):
        return {
            "id": car[0],
            "make": car[1],
            "model": car[2],
            "year": car[3],
            "status": car[4],
        }

    def get_all_cars(self, params):
        if params:
            filtered_params = list(params.items())[0]
            query = (
                f"SELECT * FROM lyfter_car_rental.cars WHERE {filtered_params[0]} = %s"
            )
            cars = self.db_manager.execute_query(query, filtered_params[1])
            return [self.__format_car(car) for car in cars]

        query = "SELECT * from lyfter_car_rental.cars"
        cars = self.db_manager.execute_query(query)
        return [self.__format_car(car) for car in cars]

    def get_car_by_id(self, car_id):
        query = "SELECT * FROM lyfter_car_rental.cars WHERE id = %s"
        car = self.db_manager.execute_query(query, car_id)[0]
        return self.__format_car(car)

    def create_car(self, *args):
        car = add_car(*args)
        print("car", car)
        return self.__format_car(car)

    def change_car_status(self, new_status, car_id):
        change_car_status(new_status, car_id)
