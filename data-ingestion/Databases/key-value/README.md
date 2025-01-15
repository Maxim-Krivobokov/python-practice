# Using Redis 
module is named Redis.redis
1) At first ,we need to create a connection.
Then test it
```python
from Redis import redis
host, port = 'localhost', 6379
conn = Redis(host=host, port=port)
if not conn.ping():
    raise SystemExit(f'error: cannot connect to redis on {host}:{port}')
```

2) then create transaction ids list
```python
transaction_ids = [
    17247,
    21332,
    30648,
    32613,
    47718,
]
```
3) search data for each transaction id:
then convert result into dict object by json.loads
and print it

```python
for tid in transaction_ids:
    key = f'tid:{tid}'
    data = conn.get(key)
    if data is None:
        print(f'{tid} not found')
        continue
    obj = json.loads(data)
    print(f'{tid}: sku={obj["sku"]}, price={obj["price"]}')
```

4) calculate all transactions in database

```python
count = 0
for _ in conn.scan_iter(match='tid:*'):
    count += 1
print(f'total of {count} transactions')
```