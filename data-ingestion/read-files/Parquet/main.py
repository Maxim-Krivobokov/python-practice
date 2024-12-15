# import pyarrow.parquet as pq ???
import parquet as pq
import pandas

def read_parquet(filename):
    """
    :param filename:
    :return: pandas dataframe object
    """
    table = pq.read_table(filename)
    df = table.to_pandas()
    return df

if __name__ == '__main__':
    data = read_parquet('taxi.parquet')
    # check column names like in CSV file
    print(data.dtypes())
