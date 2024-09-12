import redis

redis_client = redis.Redis(host="localhost",port="6379",decode_responses=True)

def set_key_in_redis(longurl,shorturl):
    redis_client.set(shorturl,longurl)

def get_key_from_redis(shorturl):
    longurl = redis_client.get(shorturl)
    return longurl