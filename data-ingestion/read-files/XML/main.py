import bz2
import xml.etree.ElementTree as xml

import pandas as pd

# Data conversions
conversion = [
    ('vendor', int),
    ('people', int),
    ('tip', float),
    ('price', float),
    ('pickup', pd.to_datetime)

]