#This areaCal file 
import ee
ee.Initialize()
import tkinter
from tkinter import *




#The function feature_loop is the outer function which loops between each of the feature elements
#This function takes in the parameters of feature,year,image,dict
#requires: feature -> object (which contains the different vector layers
#          year -> string (which is the year of extraction)
#          Image -> takes in the Image Collection which is then filtered by the year
#          mydict -> takes in the empty classification dictionary that should be populated by the area 
#          values -> this is a list which contains the values of each of the classifications

######################################################################################################################


import tkinter.ttk as ttk
    

    
    
def feature_loop(features,image,mydict,values,bar):
    
    assert(features)
    assert(image)
    assert(mydict)
    assert(values)

    #from tkinter import scrolledtext
    #result_widget = scrolledtext.ScrolledText(window, width=40,height=10)
    #result_widget.grid(column = 0, row = 0)
    #result_widget.insert(INSERT,"my text")
    
    # your script
    
    
    index = 0 #index this is important for getting the right classification value associated with its name
    dict_keys = list(mydict.keys())
    pts = 0
    prog_track = 100 / len(dict_keys) #To create lengther for progress bar
    for i in values: # for each classification type
        classification = dict_keys[index]
        index+=1
        land_class = ee.Image(image).eq(i)
        
        #land_class = ee.Image(image).updateMask(image.eq(i)) #outdated version
        
        track = 0 #just to track the progress of extraction
        track_run = len(features)
        
        for i in features: #represent each of the watershed accumlated areas 01, 02, 03
            if (track == 0):
                print("\nStarting extraction of " + classification + "\n")
            calc = feat_populate(i,land_class,mydict)
            calc = calc.getInfo()
            mydict[classification].append(calc)
            print(str(track + 1) + " of " + str(track_run)+ " completed")
            track+=1

            pts += prog_track
            
            
            def progress(pts):
                bar["value"]=pts
            bar.after(500,progress(pts))
            bar.update() #force an update



##    style = tkinter.ttk.Style() #Note changes 
##    style.theme_use('clam')
##    style.configure("green.Horizontal.TProgressbar", background='green')
##    bar2 = Progressbar(window, length=200, style = "green.Horizontal.TProgressbar", mode = "determinate") #changes of python version
##    
##    bar2.grid(row=13,column = 1)
##
##    bar
##    bar.after(500, restart(0)) #return back to fix the user interface
    bar['value'] = 0
    print("\nCOMPLETED")    
    return mydict


#This part of the code goes quite quickly



######################################################################################################################
#Please note that featureis each of the basin area for eg 01
#image is the masked image layer with the current active classification
#mydict is the constructed dictionary previously
#key is the current classification key which is going to be used to edit mydict
#https://stackabuse.com/python-nested-functions/
#nested python functions
#classify is the type of classification 
#mydict is the main storage mechanism
#web link below is where I got the idea to speed up the code to use map in python
#https://gis.stackexchange.com/questions/280682/using-python-with-google-earth-engine


#Original as of July 24, 2019 is now being utilized again
def feat_populate(feature,image,mydict):
    
    assert mydict, "Your dictionary has faults present meaning it was not created properly"
    assert feature, "You have a problem with your polygons"
    assert image, "Your classification on the image did not work"
    size = feature.size()
    feature_list = ee.List(feature.toList(size)) #This is used to further dissect the basin area into sub basins
    count = 0

    ####################################
    #New addition for better area calculation
    #https://developers.google.com/earth-engine/tutorial_forest_03
    
    ####################################

    #clipImage = ee.Image(image.clip(element.geometry()))
    imageArea = image.multiply(ee.Image.pixelArea()).divide(1000*1000)
    #Add a case for changing the reducer

    def feature_map(element):
        element = ee.Feature(element)
        shape_area = ee.Number(element.get('Shp_Area'))
        element_name = ee.String(element.get('Station')) #subject to change


        pixel_count = imageArea.reduceRegion( #Note that pixel count returns a dictionary of class type and count
                reducer = ee.Reducer.sum().unweighted(), #from .count to .sum.unweighted() for all the values to have same wieght
                geometry = element.geometry(),
                #scale = 30,
                bestEffort = True #this is for uping the maximum number of computable images
                #maxPixels =  1e10 #this could also be used but the downside is that it does not change max number of Pixels automatically
            )
        pixel_keys = ee.List(pixel_count.keys())
        area_calc = ee.Number(pixel_count.get(pixel_keys.get(0)))
        #area_calc = temp.divide(1000*1000) #changed here change to kilometres squared
        
        percent = ee.Number(area_calc.multiply(100).divide(shape_area))

        return ee.List([element_name,area_calc,percent]) #Note now shape area has been added
    map_result = feature_list.map(feature_map)
    print("Data processed: " + str(size.getInfo()))
    return map_result



