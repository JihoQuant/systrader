import json

from quantylab.systrader.creon import Creon
from quantylab.systrader.db import MongoDBClient



def run():
    # systrader에서 realtime data를 받아서 redis로 publish
    r = redis.get_client()
    def cb(item):
        r.publish('stockcur', item)
        
    c = Creon()
    coll_stockcodes = MongoDBClient.get_coll('stockcodes')
    cursor = coll_stockcodes.find({'marketcode': 1, 'active': 1}, {'_id': 0})
    codes = [item['code'] for item in list(cursor)]
    for code in codes:
        c.subscribe_stockcur(code, cb)
        

if __name__ == '__main__':
    run()
