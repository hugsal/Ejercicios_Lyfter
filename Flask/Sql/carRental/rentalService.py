class RentalService:
    def __init__(self, rental_repository):
        self.rental_repository = rental_repository

    def get_all_rentals(self, params):
        return self.rental_repository.get_all_rentals(params)

    def get_rental_by_id(self, rent_id):
        return self.rental_repository.get_rental_by_id(rent_id)

    def create_rental(self, user_id, car_id):
        return self.rental_repository.create_rental(user_id, car_id)

    def finish_rental(self, rent_id):
        return self.rental_repository.finish_rental(rent_id)

    def update_rental_status(self, rent_id, status):
        return self.rental_repository.update_rental_status(rent_id, status)
