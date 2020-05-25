################################################################################################################
#Author : Giovanni Harvey
#Last Modified Date: July 12, 2019
#Job Title: Google Earth Engine API Developer
#May 2019 - August 2019

#????????????????????????????????????????????????????????????????????????????????????????????????????????????#
"""THE USAGE OF ARCPY IS NEEDED FOR THIS MODULE THUS RUN IT FROM A COMPUTER THAT HAS ARCPY INSTALLED!!!"""
#????????????????????????????????????????????????????????????????????????????????????????????????????????????#

#########################################Purpose##############################################################

#The purpose of this module is to do a batch reprojection of the shapefiles that are going to be used
#in the coordinate extraction program.
#The projection in which it changed to is WGS 1984 or ESPG 4326 which is the commonly used coordinate representation
#for latitude and longitude.
#For example (77W,18N) would be the coordinates if one was supposed to look into google maps for Jamaica

################################################################################################################

import arcpy
from arcpy import env
import os


################################################################################################################
#Purpose
#The function main_Directory take has no parameters but requires the user to input a main folder containing the
#subfolder for the shapefiles. This function then returns a list of all the subfolder containing shapefiles.

#Flow
#PublishedBasins (Main folder) -> [01,02,03,04,05,06] (All sub folders of Published Basins)

#Requires : None -> List of strings


def main_Directory():
    print("main_Directory")
    user_input = input("Please enter the path that leads to all the shapefile folders :\n")
    os.chdir(user_input)
    directory = os.getcwd()
    sub_dir = [x[0] for x in os.walk(directory)]
    #subdir contains the list of all the list shapfile folders
    #print(sub_dir[1:len(sub_dir)])
    return sub_dir[1:len(sub_dir)]
directory = main_Directory()

################################################################################################################


################################################################################################################
#Purpose
#The function sub_Directory has the parameter directory which is the sub folder list created in the main_Directory
#function. This function then looks for all the shapefiles within each subdirectory and changes the projection from
#the original projection to WGS 1984 or ESPG 4326.

#Flow
# directory [01,02,03,04,05,06] -> 01 (one of the sub directory's) -> "####.shp"...

# Requires: Non Empty List of Strings -> None
# Effects: This function changes the projection of all the shapefiles present in the subfolders

def sub_Directory(directory):
    assert directory, "There is something wrong with your main shapefile folder"
    sr = arcpy.SpatialReference(4326)
    for shp_dir in directory:
        arcpy.env.workspace = shp_dir
        if len(arcpy.ListFiles("*.shp")) > 0:
            print(arcpy.ListFiles("*.shp"))
            count = 1
            for shapefile in arcpy.ListFiles("*.shp"):
            # Strips the '.shp' and adds scale + _.kml
                outProj = "proj_" + shapefile
                print(str(count) + " " + len(arcpy.ListFiles("*.shp"))
                arcpy.Project_management(shapefile,outProj,sr)
        else:
            arcpy.AddMessage('There are no shapefiles files in ' + arcpy.env.workspace + '.')
        

sub_Directory(directory)


################################################################################################################




