import os
import sys
import requests
from tools import *
from dotenv import load_dotenv

def main():
    load_dotenv()
    url = f"{os.getenv('API_URL')}/{get_month()}{get_year()}/{get_day()+1}"
    print(url)
    print(get_day()+1)

    resp = requests.put(url, json={
        f"{get_month()}{get_year()}": {
            get_moment(): "{:d}:{:02d}".format(get_time().hour, get_time().minute)
        }
    })

    if (resp.status_code == 200):
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()