import names
import redis
from random import randrange

def addData( r ) :
    r.set(names.get_first_name(), names.get_full_name(), ex=100)

r = redis.Redis(port='6380',password='qwerty')

while 1>0:
    addData( r )

r.close()