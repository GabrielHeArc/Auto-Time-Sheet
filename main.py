import os
import requests
from tools import *
from dotenv import load_dotenv

def main():
    load_dotenv()
    url = f"{os.getenv('API_URL')}/{get_month()}/{get_day()}"

    resp = requests.put(url, json={
        get_month(): {
            get_moment(): "{:d}:{:02d}".format(get_time().hour, get_time().minute)
        }
    })

if __name__ == "__main__":
    main()