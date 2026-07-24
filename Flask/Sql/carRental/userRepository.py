from addUser import add_user


class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def __format_user(self, user):
        return {
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "username": user[3],
            "bornDate": user[5].strftime("%d/%m/%Y"),
            "accountStatus": user[6],
        }

    def get_all_users(self, params=None):
        if params:
            filtered_params = list(params.items())[0]
            query = (
                f"SELECT * FROM lyfter_car_rental.users WHERE {filtered_params[0]} = %s"
            )
            users = self.db_manager.execute_query(query, filtered_params[1])
            return [self.__format_user(user) for user in users]

        query = "SELECT * from lyfter_car_rental.users"
        users = self.db_manager.execute_query(query)
        return [self.__format_user(user) for user in users]

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM lyfter_car_rental.users WHERE id = %s"
        user = self.db_manager.execute_query(query, user_id)[0]
        return self.__format_user(user)

    def create(self, *args):
        user = add_user(*args)
        return self.__format_user(user)

    def update_user(self, user_id, status):
        query = "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s RETURNING *"
        user = self.db_manager.execute_query(query, status, user_id)
        return self.__format_user(user)
