class RentalService:
    def __init__(self, rental_repository):
        self.rental_repository = rental_repository

    def get_all_rentals(self, params):
        return self.rental_repository.get_all_rentals(params)

    def create_rental(self, user_id, car_id):
        return self.rental_repository.create_rental(user_id, car_id)
