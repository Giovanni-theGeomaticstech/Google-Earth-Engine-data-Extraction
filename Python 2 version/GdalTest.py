################################################################################
#Author : Giovanni Harvey
#Last Modified Date : August 23, 2019
#Job Title: Google Earth Engine API Developer
#May 2019 - August 2019
################################################################################

import osgeo
import gdal
from gdal import *
from osgeo import ogr, osr
import Time_Stamp
from Time_Stamp import *


#main = [] #list to use throughout program

def shp_receiver(file_path,name):
    print("w1")
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataSource = driver.Open(file_path, 0) #0 means read-only, 1 means writeable
    layer = dataSource.GetLayer()
    sourceprj = layer.GetSpatialRef()

    #https://gis.stackexchange.com/questions/7608/shapefile-prj-to-postgis-srid-lookup-table/7615#7615
    #coordinate solution
    src = sourceprj.ExportToProj4() #The useable pyprj profection
    #print(src)
    main = [layer,src]
    result = way_two(main)
    return result

#This first way works
#https://gis.stackexchange.com/questions/54140/ogr-getx-returns-always-zero
#https://trac.osgeo.org/gdal/wiki/PythonGotchas

def way_one():
    result = []
    log("Start Program 1")
    layer2 = main[0].GetNextFeature() #use this GetNextFeature() for it to work
    geom = layer2.GetGeometryRef()
    
    for ring in geom:
        for point in range(ring.GetPointCount()):
            x,y,z = ring.GetPoint(point)
            outProj = Proj(init='epsg:4326')
            #use transform right here on the coordinates
            x2,y2 = transform(src,outProj,x,y)
            result.append([x,y])
        print("we in here")
    #print(result)
    endlog()
#way_one()

#List comprehension
#new_list = [expression for_loop_one_or_more conditions]
#faster

def helper(Point,proj_src):
    #print("helper")
    #These modules to be directly available so that it doesnot get confused with the osgeo
    import pyproj
    from pyproj import Proj,transform
    
    x,y,z = Point
    outProj = Proj(init='epsg:4326')
    #test = 
    #use transform right here on the coordinates
    x,y = transform(proj_src,outProj,x,y)
    #print(x,y)
    return [x,y]

def way_two(main):
    log("Start Coordiante Extraction")
    result = []
    layer2 = main[0].GetNextFeature() #use this GetNextFeature() for it to work
    geom = layer2.GetGeometryRef()
    for ring in geom:
        result = [helper(ring.GetPoint(point),main[1]) for point in range(ring.GetPointCount())]
    #print(result)
    endlog()
    return result
#way_two()



try:
    from osgeo import ogr, osr, gdal
except:
    sys.exit('ERROR: cannot find GDAL/OGR modules')


#https://www.reddit.com/r/gis/comments/9tdt64/extracting_x_y_coordinates_of_each_vertex_of/
# example GDAL error handler function
#http://pcjericks.github.io/py-gdalogr-cookbook/gdal_general.html#install-gdal-ogr-error-handler
##def gdal_error_handler(err_class, err_num, err_msg):
##    errtype = {
##            gdal.CE_None:'None',
##            gdal.CE_Debug:'Debug',
##            gdal.CE_Warning:'Warning',
##            gdal.CE_Failure:'Failure',
##            gdal.CE_Fatal:'Fatal'
##    }
##    err_msg = err_msg.replace('\n',' ')
##    err_class = errtype.get(err_class, 'None')
##    print ('Error Number: %s' % (err_num))
##    print ('Error Type: %s' % (err_class))
##    print ('Error Message: %s' % (err_msg))
##
##if __name__=='__main__':
##
##    # install error handler
##    gdal.PushErrorHandler(gdal_error_handler)
##
##    # Raise a dummy error
##    gdal.Error(1, 2, 'test error')
##
##    #uninstall error handler
##    gdal.PopErrorHandler()
