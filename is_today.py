import datetime as dt

def is_today(date: str):
    today = dt.datetime.now().strftime("%y-%m-%d")
    return date == today