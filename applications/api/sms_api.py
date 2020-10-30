import requests
import random
import math
import json

def generate_code():
    digits = [str(i) for i in range(0, 10)]
    random_code = ""
    for i in range(6) : 
        random_code += digits[math.floor(random.random() * 10)] 
    return str(random_code)


def get_code(telephone):
    if telephone:
        code = generate_code()
        url =  "https://sgwtaqq688.execute-api.us-east-1.amazonaws.com/dev/codesms"
        data = {
            "nbr": telephone,
            "msg": "Tu código es: " + code
        }
        headers = {
            'Content-type': 'application/json',
            'x-api-key': 'r7Yq0jEGjn8MBmsZmiKje4MhsvCD26N36vN1meVV'
            }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response, code
    else:
        return False