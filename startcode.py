
import cv2
import sys
import numpy as np
from sentinelsat import SentinelAPI

user = 'teamairo' 
password = 'a1r0-2016' 
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

products = api.query(footprint = "intersects(41.9000, 12.5000)",
                     date = ('20190601', '20190626'),
                     platformname = 'Sentinel-2',
                     processinglevel = 'Level-2A',
                     cloudcoverpercentage = (0,10)
                    )
print(products)
    
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
