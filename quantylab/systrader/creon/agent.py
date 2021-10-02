import json
import pandas as pd
import redis


r = redis.Redis(host='192.168.0.13', port=6379, db=0, charset='utf-8', decode_responses=True)


if __name__ == '__main__':
    stockranks = json.loads(r.get('stockranks'))
    df_stockranks = pd.DataFrame(stockranks['stockranks'])
    print(df_stockranks)
    pass
