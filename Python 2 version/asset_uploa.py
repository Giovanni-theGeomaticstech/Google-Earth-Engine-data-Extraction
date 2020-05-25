#-------------------------------------------------------------------------------------------------------#

#Author : Giovanni Harvey
#Last Modified Date : August 23, 2019
#Job Title: Google Earth Engine API Developer
#May 2019 - August 2019
#-------------------------------------------------------------------------------------------------------#

#This file has to do with asset management uploads to the program
#Step 1 of this program is that it is required that the shapefiles to be used are merged into one shapefile
#Step 2 of this program is then upload this shapefile into code.earthengine.google.com
# Assets -> make a folder -> then save shp
#next step is to get the name of the asset path
#Then this path will placed into a Feature Collection and added to a list




#-------------------------------------------------------------------------------------------------------#
#Imports

import ee
ee.Initialize()

import pypickle
from pypickle import *

#-------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------------------#

#for example it would be users/gioharvey14/ECtest

def asset_manage(asset_dir):
    #asset_dir 
    #asset_dir = input("Please input the asset folder path that contains your shapefiles in Earth Engine Assets: \n")
    assetList = []
    if (asset_dir == ""):
        print("You had an empty asset path")
        #asser_dir = input("Please input the asset folder path that contains your shapefiles in Earth Engine Assets: \n")
        return "There was no asset provided"
    else:
        #need to test for empty asset
        assetList.extend(ee.data.getList({'id':asset_dir})) #just to get the id of the assets

    print (assetList)

    feature_collection = [] #for storing all the newly made assets
    
    for i in assetList:
        print (type (i["id"]))
        feature_collection.append(ee.FeatureCollection(i['id']))

    return feature_collection
    #save_Object(feature_collection,"X:\WSC_BasinCharacteristics\Data\Giovanni\PublishedBasins\02")
        




#-------------------------------------------------------------------------------------------------------#


