
import cv2
import sys
import numpy as np
import bs4
import urllib
from urllib.request import urlopen
from urllib.parse import urljoin

soup = bs4.BeautifulSoup(urlopen("http://www.viewfinderpanoramas.org/dem3.html#alps"))
links = soup.find_all('a')
for link in links:
    try:
        if "/dem1/N4" in link['href']:
            url = urljoin("http://www.viewfinderpanoramas.org/", link['href'])
            filename = link['href'].split('/')[-1]
            urllib.urlretrieve(url, filename)
            #break
    except:
        print("I am error")
    
if len(sys.argv)!=2:                  ## Check for error in usage syntax
    print("Usage : python display_image.py <image_file>")

else:
    img = cv2.imread(sys.argv[1],cv2.IMREAD_COLOR)  ## Read image file
    
    try:
        if (img.any() == None):                      ## Check for invalid input
            print("Could not open or find the image")
    except AttributeError:
        if (img == None):                      ## Check for invalid input
            print("Could not open or find the image")
        else:
            cv2.namedWindow('Display Window')        ## create window for display
            cv2.imshow('Display Window',img)         ## Show image in the window
            print ("size of image: ",img.shape)        ## print size of image
            cv2.waitKey(0)                           ## Wait for keystroke
            cv2.destroyAllWindows()
    else:
        if (img.any() == None):                      ## Check for invalid input
            print("Could not open or find the image")
        else:
            cv2.namedWindow('Display Window')        ## create window for display
            cv2.imshow('Display Window',img)         ## Show image in the window        ## print size of image
            cv2.waitKey(0)                           ## Wait for keystroke
            cv2.destroyAllWindows()                  ## Destroy all windows
