import json

from quantylab.systrader.creon import Creon
from quantylab.systrader.db import MongoDBClient


c = Creon()


def run():
    coll_stockcodes = MongoDBClient.get_coll('stockcodes')
    cursor = coll_stockcodes.find({'marketcode': 1, 'active': 1}, {'_id': 0})
    codes = [item['code'] for item in list(cursor)]
    print(codes)
    c.subscribe_stockcur()
    


if __name__ == '__main__':
    run()
