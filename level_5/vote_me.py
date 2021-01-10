#!/usr/bin/python3.8
#Author Hileamlak M. Yitayew
"""this module will be used for voting 1024 timess
at the website provided that has a captcha"""


import requests
import time
from bs4 import BeautifulSoup
from PIL import Image, ImageFilter
from captcha_parser import *
from io import BytesIO

voteid = '68'
payload = {'id': voteid}
url = "http://158.69.76.135/level5.php"
captcha_url = "http://158.69.76.135/tim.php"
headers = {
    'Referer':
    url,
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'
}
captcha_bg_color = (128, 128, 128)

voted_times = 0
while voted_times < 1024:
    try:
        session = requests.session()

        site_response = session.get(url)
        captcha_response = session.get(captcha_url)

        site = BeautifulSoup(site_response.content, 'html.parser')
        captcha_img = Image.open(BytesIO(captcha_response.content))

	#Uncomment below to see what the captcha looked like
	#captcha_img.show()

        #clean up image and prepare it for text scanneing
        #substract background color
        substituteColor(captcha_img, captcha_bg_color, (0, 0, 0))
        # Brighten the bright colors more
        addvalue2Color(captcha_img, (0, 0, 0), 150)
        #find the gray scale of the image
        captcha_gray = darkend_scaled(captcha_img, 2)
        #thresh the grayscale image so that the white color would be more
        #visible
        thresh(captcha_gray, 10)
        #Blur the image to remove dots
        blurer = ImageFilter.MedianFilter(5)
        captcha_gray = captcha_gray.filter(blurer)
        #Enhance the edges
        captcha_gray = captcha_gray.filter(ImageFilter.EDGE_ENHANCE_MORE)
        
        #Uncomment the code below to see the processed image
        #captcha_gray.show()

        #extract the text in the image using tesseract
        captcha_value = tesseractOcr(captcha_gray)
       
        #find the the input tag that has the hidden type and get its value
        session_value = site.find('input', {'name': 'key'}).get('value')

        payload['key'] = session_value
        payload['captcha'] = captcha_value
        payload['holdthedoor'] = 'submit'

        r = session.post(url, data=payload, headers=headers)
        if r.status_code == 200:
            #Find the number of times voted by parsing the site
            table = list(site.findAll('tr'))[1:]
            for tr in table:
                tr_data = tr.decode_contents().split('\n')
                tr_id = tr_data[2].split(' ')[0]
                tr_votes = tr_data[4].split(' ')[0]

                if tr_id == voteid:
                    voted_times = int(tr_votes)
            print("Votes casted {} for {}".format(voted_times, voteid))

        else:
            time.sleep(1)
        del session
    except FileNotFoundError:
        time.sleep(1)
    except Exception as error:
        print(error)
        time.sleep(1)
