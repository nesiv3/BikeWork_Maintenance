import functools
import json
from infraestructure.redis_client import redis_client

def redis_cache(key_prefix: str, expire: int = 300):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{key_prefix}:{args}:{kwargs}"
            cached = redis_client.get(key)
            if cached:
                # Devuelve la lista de dicts, que FastAPI puede serializar
                return json.loads(cached)
            result = func(*args, **kwargs)
            # Si el resultado es una lista de DTOs, conviértelo a lista de dicts
            if isinstance(result, list) and hasattr(result[0], "model_dump"):
                serializable = [item.model_dump() for item in result]
            else:
                serializable = result
            redis_client.setex(key, expire, json.dumps(serializable, default=str))
            return serializable
        return wrapper
    return decorator