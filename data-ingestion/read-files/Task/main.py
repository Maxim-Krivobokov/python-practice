import bz2
import csv
import json
from collections import namedtuple
from datetime import datetime

columns = [
    Column('VendorID', 'vendor_id', int),
    Column('passenger_count', 'num_passengers', int),
    Column('tip_amount', 'tip', float),
    Column('total_amount', 'price', float),
    Column('tpep_dropoff_datetime', 'dropoff_time', parse_timestamp),
    Column('tpep_pickup_datetime', 'pickup_time', parse_timestamp),
    Column('trip_distance', 'distance', float),
]

def read_csv(filename):
    with bz2.open(filename, 'rb') as csv:
        reader = csv.DictReader(csv)
    for raw_record in reader:
        record = {}

        yield record


for i in range(5):
    data = read_csv('taxr.csv.bz2')
    print(data)
