from PIL import Image, ImageOps
import os, subprocess, tempfile, re, time

def thresh(img, threshold = 150):
     """Threshes a gray scale images
     based on threshold"""
     pixdata = img.load()
     for y in range(img.size[1]):
         for x in range(img.size[0]):
             if pixdata[x,y] > threshold:
                 pixdata[x,y] = 255
             else:
                 pixdata[x,y] = 0
def tesseractOcr(img):
    """Performs tesseract text reading to get
    the text from the image"""
    tif_file = tempfile.NamedTemporaryFile(suffix='.tif')
    img.save(tif_file.name)
    output_file = tif_file.name.replace('.tif', '.txt')
    time.sleep(1)

    subprocess.Popen(('tesseract', tif_file.name, output_file.replace('.txt', '')), stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    #subprocess.Popen(('tesseract', tif_file.name, output_file), stdout=subprocess.PIPE, stderr=subprocess.PIPE) 

    time.sleep(1)
    result = open(output_file).read()
    os.remove(output_file)
    return re.sub('[\W]', '', result)

def darkend_scaled(img, scale = 1.5):
    """"Prepares an image to be scanned for text 
    by scaling and gray scaling"""

    img = ImageOps.grayscale(img)
    width, height = img.size
    img = img.resize((int(width * scale), int(height * scale)))
    return img

