from datetime import datetime
from moment_of_day import MomentOfDay
from month import Month

def get_moment():
    hour = datetime.now().hour
    if hour <= 10:
        return MomentOfDay.START_MORNING.value
    elif hour > 10 and hour <= 12:
        return MomentOfDay.END_MORNING.value
    elif hour > 12 and hour <= 14:
        return MomentOfDay.START_AFTERNOON.value
    elif hour > 14 and hour <= 18:
        return MomentOfDay.END_AFTERNOON.value
    else:
        raise Exception("Invalid hour")

def get_month():
    date = datetime.now().month
    return Month(date).name.lower()

def get_day():
    return datetime.now().day+1

def get_time():
    return datetime.now().time()

def write_time():
    time =  datetime.now().time()
    print(time)