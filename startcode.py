
import cv2
import sys
import numpy as np
from sentinelsat import SentinelAPI
from zipfile import ZipFile

#authenticates with the website
user = 'teamairo' 
password = 'a1r0-2016' 
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

#Gets a longitude and latitude from the user
long = input("Type in a longitude: ")
lat = input("Type in a latitude: ")

#Gets a point, and asks the website for all the images of that point taken from a certain range of time
footprint = 'POINT (' + long + " " + lat + ")"
products = api.query(footprint,
                     date = ('20190601', '20190626'),
                     platformname = 'Sentinel-2',
                     processinglevel = 'Level-2A',
                     cloudcoverpercentage = (0,10)
                    )


product = list(products.keys())[0]
api.download(product)


products_df = api.to_dataframe(products)
title = products_df['title'].iloc[0]



#extracts everything from the zipfile downloaded
with ZipFile(title + '.zip', 'r') as zipObj:
   zipObj.extractall()

    
#All of this is just printing an image
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
