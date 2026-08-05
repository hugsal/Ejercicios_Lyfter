from functools import wraps
from flask import request, abort
from extension import jwt_manager


def validate_roles(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            auth = request.headers.get("Authorization")

            if not auth:
                abort(403, "Token no valido")

            parts = auth.split()
            if parts[0].lower() != "bearer":
                abort(401, "Formato de token inválido.'")

            token = parts[1]
            try:
                payload = jwt_manager.decode(token)
            except Exception as e:
                abort(401, "Token inválido")

            user_role = payload.get("role")
            if user_role not in allowed_roles:
                abort(403, "No tienes permisos suficientes para realizar esta acción")

            request.user_payload = payload
            return func(*args, **kwargs)

        return wrapper

    return decorator
