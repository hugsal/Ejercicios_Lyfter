from validations import validate_user
from datetime import datetime
from flask import abort


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_all_users(self, params=None):
        return self.user_repository.get_all_users(params)

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def create_user(self, data):
        validate_user(data)
        name = data.get("name")
        email = data.get("email")
        user_name = data.get("userName")
        password = data.get("password")
        bornDate = data.get("bornDate")
        date_val = datetime.strptime(bornDate, "%d/%m/%Y")

        users_exists = self.user_repository.get_all_users()
        for user in users_exists:
            if user["email"] == email or user["userName"] == user_name:
                abort(400, "El usuario ya existe")

        return self.user_repository.create(
            name, email, user_name, password, date_val.strftime("%Y-%m-%d")
        )

    def update_user(self, user_id, data):
        status = data.get("status")
        return self.user_repository.update_user(user_id, status)
