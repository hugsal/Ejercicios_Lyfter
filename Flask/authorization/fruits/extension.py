from jwtManager import JwtManager

with open("private_key.pem", "rb") as file:
    PRIVATE_KEY = file.read()

with open("public_key.pem", "rb") as file:
    PUBLIC_KEY = file.read()


jwt_manager = JwtManager(PRIVATE_KEY, PUBLIC_KEY)
