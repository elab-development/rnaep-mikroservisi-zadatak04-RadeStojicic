import os
from dotenv import load_dotenv
from redis_om import get_redis_connection

load_dotenv()

redis = get_redis_connection(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    decode_responses=True
)
