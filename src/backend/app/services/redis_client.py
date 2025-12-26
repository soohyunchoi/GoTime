from redis import Redis
import os

class RedisClient:
    client: Redis
    def __init__(self, redis_url):
        self.client = Redis.from_url(redis_url)

        r.set('foo', 'bar')
        value = r.get('foo')