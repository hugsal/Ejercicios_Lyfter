from functools import wraps
from flask import request, abort
from extension import jwt_manager


def validate_roles(allowed_roles):
    normalized_allowed = set(r.lower() for r in allowed_roles)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            auth = request.headers.get("Authorization")

            if not auth:
                abort(401, "Token no valido")

            parts = auth.split()
            if len(parts) != 2 or parts[0].lower() != "bearer":
                abort(401, "Formato de token invalido")

            token = parts[1]
            try:
                payload = jwt_manager.decode(token)
            except Exception as e:
                abort(401, "Token invalido o expirado")

            user_role = str(payload.get("role", "")).lower()
            if user_role not in normalized_allowed:
                abort(403, "No tienes permisos suficientes para realizar esta accion")

            request.user_payload = payload
            return func(*args, **kwargs)

        return wrapper

    return decorator
