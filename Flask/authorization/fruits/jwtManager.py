import jwt


class JwtManager:
    def __init__(self, private_key, public_key, algorithm="RS256"):
        self.private_key = private_key
        self.public_key = public_key
        self.algorithm = algorithm

    def encode(self, data):
        try:
            encoded = jwt.encode(data, self.private_key, algorithm=self.algorithm)
            return encoded
        except Exception as ex:
            print(ex)
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print(e)
            return None
