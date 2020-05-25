################################################################################
#Author : Giovanni Harvey
#Last Modified Date : August 23, 2019
#Job Title: Google Earth Engine API Developer
#May 2019 - August 2019
################################################################################

import ee
ee.Initialize()
import webbrowser
import areaCalculationSpeed
from areaCalculationSpeed import *
import Excel_Extraction2
from Excel_Extraction2 import *
import Time_Stamp
from Time_Stamp import *
import asset_uploa
from asset_uploa import *
import os
import pypickle
from pypickle import *
import tkinter
from tkinter import *
######################################################################################################################


#image = input('Please only copy the string between the circular brackets and do not include quotation marks:\n ')
#import programInterface
#from programInterface import *

#image = img_send()
#print(image)
webbrowser.open('https://developers.google.com/earth-engine/datasets/')
def makeRaster(image):
    

    #image = input('Please only copy the string between the circular brackets and do not include quotation marks:\n ')
    log("Start Program")
    

    #Please note image is the Raster Image in usage
    
  
    #simple loop to ensure that the right image tag was used
    print(image)
    
    while(True):
        if (image == ""):
            print('There was no image inputted please re-enter\n')
            #image = input('Please only copy the string between the circular brackets and do not include quotation marks\n')
            return "Error"
        elif ("ee" in image) or ("ImageCollection" in image):
            print('only copy the text in between the brackets')
            return "Error"
            #image = input('Please only copy the string between the circular brackets and do not include quotation marks\n')
        else:
            raster_layer = ee.ImageCollection(image)
            #raster_size = (raster_layer.size()).getInfo()
            return raster_layer

######################################################################################################################
def bandProperty(raster_layer):
    assert(raster_layer) #return here to make proper assertion
    
    #Temporary but needed to generate the propertyNames
    temp = raster_layer.first() #just for the purpose of getting property information
    save = temp.getInfo() #gets the meta data properties

    #This will save
    band_class = []
    for i in save['bands']:
        band_class.append(i['id'])
    return band_class
    
######################################################################################################################

######################################################################################################################


#Using the python version to get information
#This also stores the different years 

def feature_years(image):
    # finding the length of the image collection, meaning the number of bands present
    size = image.size() 
    image_list = ee.List(image.toList(size))
    
    assert image, "Your image does not exist meaning an empty layer\n" 
    #using map to get the years needed
    year_list = list(map (
                            lambda x: x['id'][len(x['id']) - 10:len(x['id'])]
                                                ,image_list.getInfo()))
    return year_list    

#stored list of years
#year_list = feature_years(image_list)
######################################################################################################################

######################################################################################################################


# In[ ]:


#The function image year takes in no parameters
#The function uses the globally created variable image year 


# In[6]:


######################################################################################################################
def image_year(year,raster_class): #Note that Year is a user selected string
    assert  year, "User did not choose a year of operation for the data" 
    size = raster_class.size() 
    image_list = ee.List(raster_class.toList(size))
    count = 0
    
    temp_list = image_list.getInfo()
    for i in temp_list:
        if (year in i['id']):
            break
        else:
            count+=1      
    image_yr = ee.Image(image_list.get(count))
    return image_yr
######################################################################################################################

######################################################################################################################



# This function will deal with the development of the classification features to be utilized

# classConstruct constructs the dictionary of the names 
# classValues contruct the values associated with each classification

# In[7]:


######################################################################################################################
def classConstruct(prop,image):
    size = image.size() 
    image_list = ee.List(image.toList(size))
    
    image_lister = (image_list.get(0)).getInfo() #Just inorder to get a sample with specified properties
    #This gives the list of properties associated with the 
    
    properties = image_lister['properties'] #getting the properties of the image
    image_class = properties[prop + "_class_names"]
    empty_class_dict = {}
    for i in image_class:
        empty_class_dict[i] = []
    return empty_class_dict
        
    #print(image_lister[user_class])
    
def classValues(prop,image):
    size = image.size() 
    image_list = ee.List(image.toList(size))
    
    image_lister = (image_list.get(0)).getInfo() #Just inorder to get a sample with specified properties
    #This gives the list of properties associated with the 
    properties = image_lister['properties'] #getting the properties of the image
    image_class = properties[prop + "_class_values"]
    class_values = []
    for i in image_class:
         class_values.append(i)
    #print(class_values)
    return class_values
######################################################################################################################    


def asset_Receive(asset):
    features = asset_manage(asset)

    if (features == []):
        print("You have no assets present\n")
        print("PROGRAM WILL NOW SHUTDOWN\n")
        exit()
    return features

######################################################################################################################


#"X:\WSC_BasinCharacteristics\Data\Giovanni\PublishedBasins\Extracted_coord0"
# This section will be used for passing the year, the image, and the feature(vector_layers)

# In[9]:


#This calculation is going to be present in another python file which makes reference to this file
#from AreaCalculation I am going to be using feature loop
#Here I will be passing on the values of FeatureList
#image_yr as the function which returns the ee.Image of the year chosen
#class construct as the empty classDictionary based on the classification chosen by the user
#classValues returns the value for each class present in the image metadata 
#def area_run():
    
    #dir(areaCalculation)
   ############################################################################################################## 
    #This was the older version as of July 22,2019
    #FeatureList[0] for the normal working dictionary
    #FeatureList[1] For the dictionary with larger coordinates
    #areaResult = feature_loop2(FeatureList[0],FeatureList[1],FeatureList[2],FeatureList[3],image_year(),classConstruct(),classValues())
    #print(areaResult)
   ##############################################################################################################
   #areaResult = feature_loop(asset_Receive(),image_year(),classConstruct(),classValues())

   #return areaResult


# This section will deal with the final Extraction into Excel

# In[11]:





# In[12]:

def extractor(dictionary,image,year):
    #save_Object(dictionary,"C:/workspace/datalab-ee/datalab/notebooks/Extraction_proj/TestersDict")
    extraction(dictionary,image,year)
    endlog() #end the time sequence
#extractor(area_run(),image,user_class[1])
 




