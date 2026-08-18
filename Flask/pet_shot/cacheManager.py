import json
import time
import redis
from functools import wraps
from flask import request
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD


class InMemoryCache:
    """Fallback cache system stored in memory with TTL tracking."""

    def __init__(self):
        self._store = {}  # key: (value, expire_timestamp)

    def get(self, key):
        if key in self._store:
            val, exp = self._store[key]
            if exp is None or time.time() < exp:
                return val
            else:
                del self._store[key]
        return None

    def set(self, key, value, ttl=None):
        exp = time.time() + ttl if ttl else None
        self._store[key] = (value, exp)

    def delete(self, key):
        self._store.pop(key, None)

    def delete_pattern(self, pattern):
        # Basic prefix wildcard matching (e.g., 'products:*')
        prefix = pattern.replace("*", "")
        keys_to_del = [k for k in self._store if k.startswith(prefix)]
        for k in keys_to_del:
            self._store.pop(k, None)

    def flush(self):
        self._store.clear()


class CacheManager:
    def __init__(self):
        self.is_redis = False
        self.client = None
        self._fallback = InMemoryCache()
        self._connect_redis()

    def _connect_redis(self):
        try:
            if REDIS_HOST:
                r = redis.Redis(
                    host=REDIS_HOST,
                    port=REDIS_PORT,
                    password=REDIS_PASSWORD or None,
                    decode_responses=True,
                    socket_timeout=1,
                )
                r.ping()
                self.client = r
                self.is_redis = True
                print("✅ CacheManager conectado exitosamente a Redis")
        except Exception as e:
            print(f"⚠️ Redis no disponible ({e}). Utilizando Fallback InMemoryCache.")
            self.is_redis = False
            self.client = self._fallback

    def get(self, key):
        try:
            if self.is_redis:
                val = self.client.get(key)
                return json.loads(val) if val else None
            return self._fallback.get(key)
        except Exception:
            return self._fallback.get(key)

    def set(self, key, value, ttl=None):
        try:
            serialized = json.dumps(value)
            if self.is_redis:
                if ttl:
                    self.client.setex(key, ttl, serialized)
                else:
                    self.client.set(key, serialized)
            else:
                self._fallback.set(key, value, ttl)
        except Exception:
            self._fallback.set(key, value, ttl)

    def delete(self, key):
        try:
            if self.is_redis:
                self.client.delete(key)
            self._fallback.delete(key)
        except Exception:
            self._fallback.delete(key)

    def delete_pattern(self, pattern):
        try:
            if self.is_redis:
                keys = self.client.keys(pattern)
                if keys:
                    self.client.delete(*keys)
            self._fallback.delete_pattern(pattern)
        except Exception:
            self._fallback.delete_pattern(pattern)

    def invalidate_products(self):
        """Invalida todos los cachés relacionados con productos."""
        self.delete_pattern("products:*")

    def invalidate_invoices(self, user_id=None):
        """Invalida cachés de facturas."""
        self.delete_pattern("invoices:*")


cache_manager = CacheManager()
