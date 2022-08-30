import sys
import redis

redis_demo = redis.StrictRedis('localhost', 6370, decode_responces=True)

header = ['firstname', 'lastname', 'fullname', 'address']

def get_values(key):
    key = str(key)
    try:
        value = redis_demo.get(key)
    except:
        sys.exit("Error in execution")
    return value

print(get_values(sys.argv[1]))