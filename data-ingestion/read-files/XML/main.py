import bz2
import xml.etree.ElementTree as xml

import pandas as pd

# Data conversions
conversion = [
    ('vendor', int),
    ('people', int),
    ('tip', float),
    ('price', float),
    ('pickup', pd.to_datetime),
    ('dropoff', pd.to_datetime),
    ('distance', float),
]

def parse_xml(file_name):
    """
    reads bzipped xml file
    parses with xml.etree func
    uses generator to save memory
    returns dict object of one ride
    """
    with bz2.open(file_name, 'rt') as f:
        tree = xml.parse(f)
    root = tree.getroot()
    for elem in root:
        record = {}
        for tag, func in conversion:
            text = elem.find(tag).text
            record[tag] = func(text)
        print(record) # Record of one ride, dict object
        yield record

def load_xml(file_name):
    """
    :param file_name:
    :return Pandas DataFrame object with XML contents:
    """
    records = parse_xml(file_name)
    return pd.DataFrame.from_records(records)

if __name__ == '__main__':
    print('Parsing bzipped xml file')
    df = load_xml('taxi.xml.bz2')
    print(df.dtypes)
    print(df.head())