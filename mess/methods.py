import time,datetime

def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

def meal_to_vote():
    now = time.gmtime()
    hrs = now[3]
    if is_time_between(time(9,0),time(12,0)):
        return "Lunch"
    elif is_time_between(time(14,0),time(20,0)):
        return "Dinner"
    elif is_time_between(time(22,0),time(6,0)) :
        return "Breakfast"
