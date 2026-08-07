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
            abort(400, "Fallo proceso de autenticacion")

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print(e)
            raise ValueError("Token expirado")
