import datetime

def long_to_datetime(timestamp): 
    dt = datetime.datetime.fromtimestamp(timestamp / 1000)
    return dt.isoformat