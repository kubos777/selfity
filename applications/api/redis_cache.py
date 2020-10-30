import redis
import pickle

redis_conn = redis.Redis(
    host='redis-18262.c240.us-east-1-3.ec2.cloud.redislabs.com',
    port=18262,
    password='kub0s911'
)

def create_tmp_code(telephone_code):
    data = pickle.dumps(telephone_code)
    name_code = "code-"+telephone_code['code']
    redis_conn.set(name_code,data,300)

def set_session(telephone_access_token):
    data = pickle.dumps(telephone_access_token)
    name_session = "session-"+str(telephone_access_token['telephone'])
    redis_conn.set(name_session,data,600)

def session_exists(telephone_number):
    name_session = "session-"+str(telephone_number)
    data = redis_conn.get(name_session)
    if data:
        return True
    else: 
        return False

def code_exists(code):
    name_code = "code-"+ str(code)
    data = redis_conn.get(name_code)
    data_dict = pickle.loads(data)
    if data and data_dict['code'] == str(code):
        return True
    else: 
        return False

