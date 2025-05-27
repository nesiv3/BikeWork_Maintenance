import redis
import os
from dotenv import load_dotenv

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL")
REDIS_PORT = os.getenv("REDIS_PORT")

REDIS_USERNAME:str = os.getenv("REDIS_NAME","").strip()
REDIS_PASSWORD:str = str(os.getenv("REDIS_PASS").strip())

redis_client = redis.Redis(
    host=REDIS_URL,
    port=REDIS_PORT,
    decode_responses=True,
    username=REDIS_USERNAME,
    password=REDIS_PASSWORD,
)



