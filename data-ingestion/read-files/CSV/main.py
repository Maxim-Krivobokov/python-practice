# may use pandas or built-in library methods

# imports for  Built-in methods
import bz2
import csv
from collections import namedtuple
from datetime import datetime

# imports for pandas
import pandas as pd


Column = namedtuple('Column', 'src dest convert')

def parse_timestamp(text):
    return datetime.strptime(text, '%Y-%m-%d %H:%M:%S')

# First is real column in CSV. second- python variable name, third = type
columns = [
    Column('VendorID', 'vendor_id', int),
    Column('passenger_count', 'num_passengers', int),
    Column('tip_amount', 'tip', float),
    Column('total_amount', 'price', float),
    Column('tpep_dropoff_datetime', 'dropoff_time', parse_timestamp),
    Column('tpep_pickup_datetime', 'pickup_time', parse_timestamp),
    Column('trip_distance', 'distance', float),
]

def iter_records(file_name):
    """
    takes bzipped .csv file and reads content
    returns data with generator, to save memory
    """
    with bz2.open(file_name, 'rt') as fp:
        reader = csv.DictReader(fp)
        for csv_record in reader:
            record = {}
            for col in columns:
                # col is instance of Column class (as namedtuple)
                value = csv_record[col.src]
                record[col.dest] = col.convert(value)
            yield record

def example():
    """
    func to test reading CSV file using iter_records
    """
    from pprint import pprint

    for i, record in enumerate(iter_records('taxi.csv.bz2')):
        if i >= 10:
            break
        pprint(record)

# Run example with built-in csv
#example()

def load_csv_pandas(filename):
    """
    read csv file using pandas
    whole file is stored in memory
    """
    #print(df.dtypes) # by default timestamps wold be text with type 'object', we must convert them to datetime type
    time_cols = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']
    #df = pd.read_csv(filename, parse_dates=time_cols, chunksize=1000)
    df = pd.read_csv(filename, parse_dates=time_cols)
    # see all columns and types
    print(df.dtypes)

def load_csv_chunk(filename):
    """
    read csv by chunk
    return chunk with generator
    """
    yield from pd.read_csv(filename, chunksize=1000)


#load_csv_pandas('taxi.csv.bz2')

for i, df in enumerate(load_csv_chunk('taxi.csv.bz2')):
    if i > 10:
        break
    print(len(df))
    #print(df)
    

