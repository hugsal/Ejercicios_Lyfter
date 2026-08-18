import redis


class CacheManager:
    def __init__(self, host, port, password, *args, **kwargs):
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            password=password,
            *args,
            **kwargs,
        )
        connection_status = self.redis_client.ping()
        if connection_status:
            print("Cache connection created successfully")

    def store_list(self, key, data):
        try:
            self.redis_client.sadd(key, *data)
        except redis.RedisError as error:
            print(f"An error occurred while storing list in Redis: {error}")

    def store_data(self, key, value, time_to_live=None):
        try:
            if time_to_live is None:
                self.redis_client.set(key, value)
            else:
                self.redis_client.setex(key, time_to_live, value)
        except redis.RedisError as error:
            print(f"An error occurred while storing data in Redis: {error}")

    def get_all_data(self, keys):
        try:
            outputs = self.redis_client.mget(keys)
            if outputs is not None:
                result = [
                    output.decode("utf-8") if output else None for output in outputs
                ]
                return result
            else:
                return None
        except redis.RedisError as error:
            print(f"An error occurred while retrieving all data from Redis: {error}")

    def get_list_data(self, key):
        try:
            outputs = self.redis_client.smembers(key)
            if outputs is not None:
                output_list = list(outputs)
                result = [
                    output.decode("utf-8") if output else None for output in output_list
                ]
                return result
            else:
                return None
        except redis.RedisError as error:
            print(f"An error occurred while retrieving list from Redis: {error}")

    def get_data(self, key):
        try:
            output = self.redis_client.get(key)
            if output is not None:
                result = output.decode("utf-8")
                return result
            else:
                return None
        except redis.RedisError as error:
            print(f"An error occurred while retrieving data from Redis: {error}")

    def delete_data(self, key):
        try:
            output = self.redis_client.delete(key)
            return output == 1
        except redis.RedisError as error:
            print(f"An error occurred while deleting data from Redis: {error}")
            return False

    def delete_from_list(self, key, value):
        try:
            output = self.redis_client.srem(key, value)
            return output == 1
        except redis.RedisError as error:
            print(
                f"An error occurred while deleting element from list from Redis: {error}"
            )
            return False
