from datetime import datetime
import os
import requests

import urllib.parse
from moment_of_day import MomentOfDay
from month import Month

def get_moment(full=False):
    hour = datetime.now().hour
    if hour <= 9:
        if not full:
            return MomentOfDay.START_MORNING.value
        else:
            return MomentOfDay.START_MORNING_FULL.value
    elif hour >= 10 and hour <= 12:
        if not full:
            return MomentOfDay.END_MORNING.value
        else:
            return MomentOfDay.END_MORNING_FULL.value
    elif hour > 12 and hour <= 14:
        if not full:
            return MomentOfDay.START_AFTERNOON.value
        else:
            return MomentOfDay.START_AFTERNOON_FULL.value
    elif hour > 14:
        if not full:
            return MomentOfDay.END_AFTERNOON.value
        else:
            return MomentOfDay.END_AFTERNOON_FULL.value
    else:
        raise Exception("Invalid hour")

def get_month():
    date = datetime.now().month
    return Month(date).name.lower()

def get_day():
    return datetime.now().day

def get_time():
    return datetime.now().time()

def get_year():
    return datetime.now().year

def send_notification(message):
    """
    Summary : Send message to telegram
    :param message: message to send
    :return: True if message is sent, False if not
    """
    url = f"https://api.telegram.org/bot{os.environ.get('TOKEN_BOT_TELEGRAM')}/sendMessage?chat_id={os.environ.get('CHAT_ID_TELEGRAM')}&text={message}"
    response = requests.get(url)  # this sends the message
    return True if response.status_code == 200 else False