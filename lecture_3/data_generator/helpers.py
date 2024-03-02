from datetime import datetime
import random

def random_date(year):
    start = datetime(year, 1, 1)
    end = datetime(year, 12, 31)
    return start + (end - start) * random.random()

def data_saver(df, filename):
    df.to_excel(filename, index = False)