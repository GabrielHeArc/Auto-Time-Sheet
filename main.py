import os
import requests
from tools import *
from dotenv import load_dotenv

def main():
    load_dotenv()
    url = f"{os.getenv('API_URL')}/{get_month()}{get_year()}/{get_day()+1}"

    resp = requests.put(url, json={
        f"{get_month()}{get_year()}": {
            get_moment(): "{:d}:{:02d}".format(get_time().hour, get_time().minute)
        }
    })

    if (resp.status_code == 200):
        pass

    else:
        pass

    get_insert = requests.get(url)
    data = get_insert.json()[f"{get_month()}{get_year()}"][get_moment()]

    if (data == "{:d}:{:02d}".format(get_time().hour, get_time().minute)):
        send_notification(f"Hour inserted in {get_moment(True)}: " + "{:d}:{:02d}".format(get_time().hour, get_time().minute))
        print("Success")
    else:
        send_notification(f"Error while insert hour in {get_moment(True)}")
        print("Failure")

if __name__ == "__main__":
    main()