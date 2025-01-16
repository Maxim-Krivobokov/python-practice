"""Finding outliers manually"""
import sqlite3

import pandas as pd

# Load data from database
conn = sqlite3.connect('rides.db', detect_types=sqlite3.PARSE_DECLTYPES)
df = pd.read_sql('SELECT * FROM rides', conn)
conn.close()


print('.9 percentile', df['trip_distance'].quantile(.9))  # 7.06
print('max', df['trip_distance'].max())  # 932.9 - too large ride disatnce, thats an non-correct value

# Change all rides above 100miles to .99 quantile
mask = df['trip_distance'] > 100
print('num outliers:', len(df[mask]))  # 7

fill_value = df['trip_distance'].quantile(.99)
print('fill_value =', fill_value)  # 19.48

print(df.loc[mask, 'trip_distance']) # Check all 'unreal' trip distances - 7 of them
df.loc[mask, 'trip_distance'] = fill_value # Every value will be replaced with 19.48

# Check them after changing to .99 quantile
print(df.loc[mask, 'trip_distance'])

# Check new max distance after repair
print('max after fix', df['trip_distance'].max())  # 35.57 that maximum trip distance seems to be fair.
