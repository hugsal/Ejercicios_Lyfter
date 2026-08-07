from jwtManager import JwtManager
from cacheManager import CacheManager
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

with open("private_key.pem", "rb") as file:
    PRIVATE_KEY = file.read()

with open("public_key.pem", "rb") as file:
    PUBLIC_KEY = file.read()


jwt_manager = JwtManager(PRIVATE_KEY, PUBLIC_KEY)

cache_manager = CacheManager(REDIS_HOST, REDIS_PORT, REDIS_PASSWORD)
