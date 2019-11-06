import time
import pickle
from uuid import uuid4
from redis import Redis, BlockingConnectionPool
from . import config


redis_conn = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    connection_pool=BlockingConnectionPool(max_connections=config.REDIS_POOL_SIZE),
)


def get_task_result(token):
    return pickle.loads(redis_conn.get("result:" + token))


def enqueue_randomize_image_task(image_bytes):
    task_token = uuid4().hex

    redis_conn.set("result:" + task_token, pickle.dumps({"status": "requested"}))
    redis_conn.rpush(
        "tasks",
        pickle.dumps(
            {
                "func": "randomize_image",
                "token": task_token,
                "payload": {"data": image_bytes},
            }
        ),
    )

    return task_token
