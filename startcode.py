
import cv2
import sys
import numpy as np
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from zipfile import ZipFile
import glob
import rasterio as rio
import folium
import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon

#authenticates with the website
alpha = 'teamairo' 
beta = 'a1r0-2016' 
api = SentinelAPI(alpha, beta, 'https://scihub.copernicus.eu/dhus')

#Gets a longitude and latitude from the user

footprint = geojson_to_wkt(read_geojson('swiss_zip.geojson'))
    
products = api.query(footprint,
                     date = ('20190601', '20190626'),
                     platformname = 'Sentinel-2',
                     processinglevel = 'Level-2A',
                     cloudcoverpercentage = (0,10)
                    )


product = list(products.keys())[0]
api.download(product)

#this turns the list of satellite images into a database and takes the title of the first one so the zipfile can be recognized
products_df = api.to_dataframe(products)
title = products_df['title'].iloc[0]

#extracts everything from the zipfile downloaded
with ZipFile(title + '.zip', 'r') as zipObj:
   zipObj.extractall()

#Finding all the files that we can combine into an image
list = glob.glob('**/*.jp2', recursive=True)

b2 = rio.open(list[1])
b3 = rio.open(list[2])
b4 = rio.open(list[3])
print(list[2])

with rio.open('RGB.tiff','w',driver='Gtiff', width=b4.width, height=b4.height, 
              count=3,crs=b4.crs,transform=b4.transform, dtype=b4.dtypes[0]) as rgb:
    rgb.write(b2.read(1),1) 
    rgb.write(b3.read(1),2) 
    rgb.write(b4.read(1),3) 
    rgb.close()
    
with rio.open('RG.tiff','w',driver='Gtiff', width=b4.width, height=b4.height, 
              count=3,crs=b4.crs,transform=b4.transform, dtype=b4.dtypes[0]) as rgb:
    rgb.write(b2.read(1),1) 
    rgb.close()
    

    
#All of this is just printing an image
img = cv2.imread('RGB.tiff',cv2.IMREAD_COLOR)  ## Read image file
    
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
