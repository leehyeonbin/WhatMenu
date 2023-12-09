import datetime as dt

def is_today(date: str):
    today = dt.datetime.now().strftime("%y-%m-%d")
    print("{} == {} = {}".format(date, today, date == today))
    return date == today