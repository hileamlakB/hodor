#!/usr/bin/python3.8
#Author Hileamlak M. Yitayew

"""this module will be used for voting 1024 times
at the website provided"""
import requests
import time

payload = {'id': '68', 'holdthedoor': 'Submit'}

i = 0
while i < 1024:
    r = requests.post("http://158.69.76.135/level0.php", data=payload)
    if r.status_code == 200:
        i += 1
        print("Votes casted {}".format(i))
    else:
        time.sleep(1)

