import bz2
import logging
import re
from datetime import datetime

def parse_line(line):
    """
    :param line: gets raw text string from logs, compares to regexp pattern
    :return:  dict object with ride details
    """
    # Example:
    # Ride of 1 passenger started ay 2018-10-31T07:10:55 and paid $20,54
    match = re.search(r'(\d+) pass.*started at ([^ ]+).*paid \$(\d+\.\d+)', line)
    if not match:
        return None

    return {
        'count': int(match.group(1)),
        'start': datetime.fromisoformat(match.group(2)),
        'amount': float(match.group(3)),
    }

def iter_rides(file_name):
    """
    :param file_name: - bz2 file of text logs
    iterates on each line of the logs, parses it with parse_line func
    :return: - record - dict object with one reide details. Uses yield to save memory
    """
    with bz2.open(file_name, 'rt') as fp:
        for line_num, line in enumerate(fp, 1):
            record = parse_line(line)
            if not record:
                logging.warning('%s: cannot parse line', line_num)
                continue
            yield record

if __name__ == '__main__':
    from pprint import pprint

    for n, ride in enumerate(iter_rides('taxi.log.bz2')):
        if n > 5:
            break
        pprint(ride)