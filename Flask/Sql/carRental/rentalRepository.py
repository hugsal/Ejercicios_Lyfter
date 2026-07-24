class RentalRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def __format_rental(self, rental):
        return {
            "id": rental[0],
            "rentedDate": rental[1].strftime("%d/%m/%Y"),
            "rentalStatus": rental[2],
            "userId": rental[3],
            "carId": rental[4],
        }

    def get_all_rentals(self, params):
        if params:
            filtered_params = list(params.items())[0]
            query = f"SELECT * FROM lyfter_car_rental.user_car_rent WHERE {filtered_params[0]} = %s"
            rentals = self.db_manager.execute_query(query, filtered_params[1])
            return [self.__format_rental(rental) for rental in rentals]

        query = "SELECT * FROM lyfter_car_rental.user_car_rent"
        rentals = self.db_manager.execute_query(query)
        return [self.__format_rental(rental) for rental in rentals]

    def create_rental(self, user_id, car_id):
        query = "INSERT INTO lyfter_car_rental.user_car_rent (fk_user_id, fk_car_id) VALUES (%s, %s) RETURNING *"
        rental = self.db_manager.execute_query(query, user_id, car_id)
        return self.__format_rental(rental)
