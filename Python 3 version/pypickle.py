#####################################################################################################################
# Author : Giovanni Harvey
# Date of Last modification : July 12, 2019
################################################################################################################
#Author : Giovanni Harvey
#Last Modified Date: July 12, 2019
#Job Title: Google Earth Engine API Developer
#May 2019 - August 2019
################################################################################################################

#####################################################################################################################
import pickle
from pickle import *
import ee
ee.Initialize()
import sys
import os

#please note that name is a string
#Save the object
def save_Object(object_,name):
    assert object_
    assert name
    pickle_out = open(name + ".pickle","wb") #open a file to write bytes
    pickle.dump(object_,pickle_out)
    pickle_out.close()
    print("Done with object " + name)
    return name

#Open the object
#requires the the path which is the name to be utilizing a backard slash /
def read_Object(name):
    assert name,"Name error"
    sys.setrecursionlimit(50000)
    # put error handle here for recursion limit
    if (".pickle" in name):
        pickle_in = open(name,"rb")
    else:
        pickle_in = open(name + ".pickle","rb")
    object_ = pickle.load(pickle_in)
    print("Object " + name + " loaded")
    return object_
