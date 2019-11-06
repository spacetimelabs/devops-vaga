import os


REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_POOL_SIZE = int(os.getenv("REDIS_POOL_SIZE", "20"))
