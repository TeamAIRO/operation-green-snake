
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
"""alpha = 'teamairo' 
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
    
"""

imagename = input("image name:")
image = cv2.imread(imagename,cv2.IMREAD_COLOR)  ## Read image file
    

boundaries = [
	([27,0, 98], [252, 229, 210])
]

for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
        
	
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
	
nPixels = np.count_nonzero(mask == 0)
count = mask.size
percentage = nPixels/count
if percentage < 0.9:
	print("This is suitable for trees")
	
print(percentage)
		
	
	
