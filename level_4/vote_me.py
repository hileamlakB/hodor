#!/usr/bin/python3.8
#Author Hileamlak M. Yitayew

"""this module will be used for voting 4096 times
at the website provided"""
import requests
import time
from bs4 import BeautifulSoup
from proxy_generator import generate_proxys 


voteid = '68'
payload = {'id': voteid}
url = "http://158.69.76.135/level4.php"
headers = {'Referer': url,'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}

filename = "proxies.txt"
generate_proxys(filename)

proxy_list = []
with open(filename, 'r') as proxy_file:
    proxy_list = proxy_file.read().split('\n')
print("Generated_proxy_list")
#print(proxy_list)
i = 0
j = -1
voted_times = 0
while voted_times < 98:
    try:
        session = requests.session()

        response = session.get(url)
        site = BeautifulSoup(response.content, 'html.parser')

        #find the input tag that has the hidden type and get its value
        value = site.find('input',{'name':'key'}).get('value')
        payload['holdthedoor']='submit'
        payload['key'] = value

        j += 1
        r = session.post(url, data=payload, headers=headers, proxies={'http':proxy_list[j], 'https':proxy_list[j]}, timeout = 6)
        if r.status_code != 200:
            time.sleep(1)
        else:
            #Find the number of times 
            table = list(site.findAll('tr'))[1:]
            for tr in table:
                tr_data = tr.decode_contents().split('\n')
                tr_id = tr_data[2].split(' ')[0]
                tr_votes = tr_data[4].split(' ')[0]

                if tr_id == voteid:
                    voted_times = int(tr_votes)
            print("Votes casted {} for {}".format(voted_times, voteid))
        
        del session
    except Exception as error:
        print(error)
        time.sleep(1)
