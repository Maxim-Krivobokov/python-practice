# sqlite
embedded database, thatcomes inside standart lib

# TODO: learn basic sqlite3 CLI commands

```sh
# open db file and start intercative shell
sqlite3 file.db
# get full list of commands
.help

# show schema
.schema
```

# Working with sqlite3 in python
script: rides.py

1) create a connection
```python
conn = sqlite3.connect('file.db', detect_types=sqlite3.PARSE_DECLTYPES)
```
2) row_factory - for getting rows as dictionaries, accessing column by name
```python
conn.row_factory = sqlite3.Row
```

3) prepare an query:
```python
params = {'vendor': 'VeriFone',}
sql = 'SELECT distance FROM rides WHERE vendor = :vendor'
# substitution will happen here :vendor => VeriFone
```
4) create cursor and execute the query
```python
cur = conn.cursor()
cur.execute(sql, params)
```
5) Now we can iterate on the rows:
# We got all rows with vendor = VeriFone
```python
total, count = 0, 0
for row in cur:
    total += row['distance']
    count += 1
```
6) Calculate average distance
```
avg_distance = total/count
print(f'{avg_distance.2f} miles')
```

# Working with sqlite3 with pandas
script: rides_pd.py
steps 1-3 are the same

4) create dataframe from sql query response:
```python
df = pd.read_sql(sql, conn, params=params)
```
5) calculate average distance using dataframe method '.mean()'
```python
avg_distance = df['distance'].mean()

```