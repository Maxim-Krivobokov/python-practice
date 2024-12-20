"""Working with Redis"""
import json

from redis import Redis

host, port = 'localhost', 6379

conn = Redis(host=host, port=port)
if not conn.ping():
    raise SystemExit(f'error: cannot connect to redis on {host}:{port}')

# Find data on specific transactions
transaction_ids = [
    17247,
    21332,
    30648,
    32613,
    47718,
]

for tid in transaction_ids:
    # access to redis db is by keys in format: 'tid:12345'
    key = f'tid:{tid}'
    # conn.get returns Json string or None
    data = conn.get(key)
    if data is None:
        print(f'{tid} not found')
        continue
    obj = json.loads(data) # convert Josn string to dict object
    print(f'{tid}: sku={obj["sku"]}, price={obj["price"]}')

# How much data do we have
count = 0
for _ in conn.scan_iter(match='tid:*'):
    count += 1
print(f'total of {count} transactions')
