from datetime import datetime
from time import sleep
import requests


while True:
    requests.get('https://www.google.com/')
    print(datetime.now())
    sleep(2)
