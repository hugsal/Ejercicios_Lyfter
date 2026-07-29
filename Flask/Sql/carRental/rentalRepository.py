from finishRent import finish_rent


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

    def get_rental_by_id(self, rent_id):
        query = "SELECT * FROM lyfter_car_rental.user_car_rent WHERE id = %s"
        rentals = self.db_manager.execute_query(query, rent_id)
        if not rentals:
            return None
        return self.__format_rental(rentals[0])

    def create_rental(self, user_id, car_id):
        query = "INSERT INTO lyfter_car_rental.user_car_rent (fk_user_id, fk_car_id) VALUES (%s, %s) RETURNING *"
        rental = self.db_manager.execute_query(query, user_id, car_id)
        return self.__format_rental(rental)

    def finish_rental(self, rent_id):
        rental = finish_rent(rent_id)
        if not rental:
            return None
        return self.__format_rental(rental)

    def update_rental_status(self, rent_id, status):
        query = "SELECT fk_car_id FROM lyfter_car_rental.user_car_rent WHERE id = %s"
        result = self.db_manager.execute_query(query, rent_id)
        if not result:
            return None
        car_id = result[0][0]

        if status == "finished":
            update_car_query = (
                "UPDATE lyfter_car_rental.cars SET status = 'ready' WHERE id = %s"
            )
            self.db_manager.execute_query(update_car_query, car_id)

        update_rent_query = "UPDATE lyfter_car_rental.user_car_rent SET rent_status = %s WHERE id = %s RETURNING *"
        rental = self.db_manager.execute_query(update_rent_query, status, rent_id)
        return self.__format_rental(rental)
