#!/usr/bin/python3.8
#Author Hileamlak M. Yitayew

"""this module will be used for voting 1024 timess
at the website provided that has a captcha"""
import requests
import time
from bs4 import BeautifulSoup
from PIL import Image, ImageOps
from captcha_parser import thresh, tesseractOcr, darkend_scaled
from io import BytesIO



payload = {'id': '68'}
url = "http://158.69.76.135/level3.php"
captcha_url = "http://158.69.76.135/captcha.php"
headers = {'Referer': url,'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}


i = 0
while i < 1024:
    try:
        session = requests.session()

        site_response = session.get(url)
        captcha_response = session.get(captcha_url)

        site = BeautifulSoup(site_response.content, 'html.parser')
        captcha_img = Image.open(BytesIO(captcha_response.content))

        #clean up image and prepare it for text scanneing
        captcha_gray = darkend_scaled(captcha_img)
        thresh(captcha_gray)

        #captcha_gray.show()
        captcha_value = tesseractOcr(captcha_gray)

        #find the the input tag that has the hidden type and get its value
        session_value = site.find('input',{'name':'key'}).get('value')

        payload['key'] = session_value
        payload['captcha'] = captcha_value
        payload['holdthedoor']='submit'

        r = session.post(url, data=payload, headers=headers)
        if r.status_code == 200:
            i += 1
            print("Votes casted {}".format(i))
        else:
            time.sleep(1)
        del session
    except FileNotFoundError:
    	time.sleep(1)
    except Exception as error:
        print(error)
        time.sleep(5)
