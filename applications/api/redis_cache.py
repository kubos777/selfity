import redis
import pickle

redis_conn = redis.Redis(
    host='redis-18262.c240.us-east-1-3.ec2.cloud.redislabs.com',
    port=18262,
    password='kub0s911'
)

def create_tmp_code(telephone_code):
    data = pickle.dumps(telephone_code)
    redis_conn.set("data",data,300)
