import json
from datetime import datetime, timedelta

durations = []

def parse_time(ts):
    """
    raw time '2018-10-31T07:10:55.000Z'
    :return: converted time in proper format:
    datetime.datetime(2018, 10, 31, 7, 10, 55)
    """
    # trim out Z suffix
    return datetime.fromisoformat(ts[:-1])

def fix_pair(pair):
    """
    :param pair: pair of key and value of json object;
    :return: the same pair, or key with converted datetime, if key is related to pickup or dropoff
    """
    key, value = pair
    if key not in ('pickup', 'dropoff'):
        return pair
    return key, parse_time(value)

def pairs_hook(pairs):
    """
    :param pairs: key-values pairs
    :return: dict-object: converted pairs (datetime is transformed)
    """
    return dict(fix_pair(pair) for pair in pairs)


def main():
    """
    reading json logs file line by line. Each string has a JSON format and can be DE-serialized string to python object type
    custom object hooks allows to transform raw datetime to proper format, that suits to datetime and delta methods
    """
    print('Reading json logs')
    with open('taxi.jl') as fp:
        for line in fp:
            obj = json.loads(line, object_pairs_hook=pairs_hook)
            duration = obj['dropoff'] - obj['pickup']
            durations.append(duration)
    avg_duration = sum(durations, timedelta()) / len(durations)
    print(f'average ride durations: {avg_duration}')

if __name__ == '__main__':
    main()