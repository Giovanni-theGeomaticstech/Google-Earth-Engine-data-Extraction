################################################################################
#Author : Giovanni Harvey
#Last Modified Date : August 23, 2019
#Job Title: Google Earth Engine API Developer
#May 2019 - August 2019
################################################################################




import sys
import tkinter
from tkinter import *
import main_Program
from main_Program import *
import areaCalculationSpeed
from areaCalculationSpeed import *
#import asset_uploa
#from asset_uploa import *
import ee
ee.Initialize()

interStor = {"Buttons":[],"Entry":[],"Label":[],"Text":[], "Results" :[""],"Progress_Bar":None}

#storage_list_1 = [] # this is for the retrieval of the Raster information result associated with all its buttons







    

    

#def interface_set():
    
    
window = Tk()
window.title("Earth Engine Extraction")
window.geometry("600x400")

##############################################################################################################


def img_release():

    success = "Thank you Image Input Received!"
    #result = interStor["Results"][0]
    result = value
    interStor['Img_name'] = result.get()
    
    label_2 = Label(window,text="The image chosen was: " + result.get(), font = ("Comic Sans Ms",10))
    label_2.grid(row=0,column=2)       
   
    
    raster_layer = makeRaster(result.get())
    if (raster_layer == "Error"):
        interStor["Label"][0].configure(text = "Image was not created please re-enter image")
    else:
        interStor["Label"][0].configure(text = success)
        interStor["Results"][0] = raster_layer
        interStor["Entry"][0].delete(0,END) #CLear the Entry Box
        #########################Getting the band properties####################################################
        bandProp = bandProperty(raster_layer)
        if (len(interStor["Results"])==1): 
            interStor["Results"].append(bandProp)
        else:
            interStor["Results"][1] = bandProp
    #print(interStor["Results"])


    property_menu(raster_layer)
    
    


######################################################Property bands##############################################
def property_menu(raster_layer):

    window.geometry("900x450")
    Label_2.grid(row=5,column=0)

    temp = StringVar()
    propbox = OptionMenu(window,temp,*interStor["Results"][1])
    propbox.grid(row=5,column=1)
    
    def change_dropdown(*args):
        print("You chose to use " + temp.get() + " as your band classification\n")

        raster_class = raster_layer.select(temp.get())
        if (len(interStor["Results"]) == 2):
            interStor["Results"].append([temp.get(),raster_class])
        else:
            interStor["Results"][2] = [temp.get(),raster_class]
        
        #print(interStor["Results"])
        
        
        year_list = feature_years(interStor["Results"][2][1])
        year_menu(year_list)
    temp.trace('w',change_dropdown)

    
    

##################################################################################################################

def year_menu(year):
    Label_3.grid(row=5,column=2)
    temp = StringVar()
    propbox = OptionMenu(window,temp,*year)
    propbox.grid(row=5,column=3)

    def change_dropdown(*args):
        print("You chose to use " + temp.get() + " as your year\n")

        interStor["year"] = temp.get()
        raster_class = interStor["Results"][2][1]
        prop = interStor["Results"][2][0]
        
        raster_with_year = image_year(temp.get(),raster_class) #Raster with year applied to it

        


        if (len(interStor["Results"]) == 3): 
                interStor["Results"].append(raster_with_year)
        else:
                interStor["Results"][3] = raster_with_year
        #print(interStor["Results"])

        
        class_names = classConstruct(prop,raster_class)
        class_values = classValues(prop,raster_class)
        
        index_check(class_names,class_values)

    def index_check(class_names,class_values):
        if (len(interStor["Results"]) == 4): 
                interStor["Results"].append(class_names)
        else:
                interStor["Results"][4] = class_names
        #print(interStor["Results"])

        if (len(interStor["Results"]) == 5): 
                interStor["Results"].append(class_values)
        else:
                interStor["Results"][5] = class_values
        #print(interStor["Results"])

        
        
    temp.trace('w',change_dropdown)
    
    
    
    

############################################For the Raster Collection##################################################################
#For the initial button data

label_1 = Label(window,text = "Input Google Earth Image:",font=("Arial Bold",10))
button_1 = Button(window,text="Raster Retrieval",command = img_release) #Going to have the text and the button in the same line  
value = StringVar()
entry_1 = Entry(window,text = value,width=40) #value


interStor["Results"].append("")
interStor["Buttons"].append(button_1)
interStor["Label"].append(label_1)                
interStor["Entry"].append(entry_1)
    

label_1.grid(row=0,column=0)
entry_1.grid(row=0,column=1)
button_1.grid(row=2,column=1)


##############################################################################################################


######################################For the Area calculation########################################################################

def extraction():
    #txt_2.insert(END,assets.get() + "\n")
    image_year = interStor["Results"][3]
    classConst = interStor["Results"][4]
    classVal = interStor["Results"][5]
    extract_result = feature_loop(asset_Receive("users/" + assets.get()),image_year,classConst,classVal,bar)
    interStor["Extracted"] = extract_result

    bar2["value"] = 100
    bar2.grid(row=13,column = 1)
    
def display_results():
    bar2.grid_remove()
    dictionary = interStor["Extracted"]
    img_name = interStor['Img_name']
    year = interStor["year"]
    extractor(dictionary,img_name,year)
######################################################################################################################
    
Label_2 = Label(window,text = "Choose a classification type for your image",font=("Comic Sans Ms",10))
Label_3 = Label(window,text = "Choose a year to be used for your image",font=("Comic Sans Ms",10))

button_2 = Button(window,text="Click me for Extraction",command = extraction)
button_3 = Button(window,text="Display Results",command = display_results,bg="black",fg="white")



assets = StringVar()
Label_4 = Label(window,text = "Shapefile Asset folder: users/",font=("Comic Sans Ms",10))
entry_2 = Entry(window,text=assets,width=40)

Label_4.grid(row=8,column=0)
entry_2.grid(row=8,column=1)


button_2.grid(row=11,column=1)
button_3.grid(row=18,column=1)




if sys.version_info[0] < 3:
    import tkinter.ttk as ttk
    style = ttk.Style()
    style.theme_use('default')
    style.configure("red.Horizontal.TProgressbar", background='red')
    bar = ttk.Progressbar(window, length=200, style="red.Horizontal.TProgressbar", mode = "determinate")
    bar['value'] = 0
    bar.grid(row=13,column = 1)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("green.Horizontal.TProgressbar", background='green')
    bar2 = ttk.Progressbar(window, length=200, style = "green.Horizontal.TProgressbar", mode = "determinate")
else:
    from tkinter.ttk import *
    style = tkinter.ttk.Style()
    style.theme_use('clam')
    style.configure("red.Horizontal.TProgressbar", background='red')
    bar = Progressbar(window, length=200, style="red.Horizontal.TProgressbar", mode = "determinate")
    bar['value'] = 0
    bar.grid(row=13,column = 1)

    style = tkinter.ttk.Style()
    style.theme_use('clam')
    style.configure("green.Horizontal.TProgressbar", background='green')
    bar2 = Progressbar(window, length=200, style = "green.Horizontal.TProgressbar", mode = "determinate")
#######################################Scrolled Process#########################################################




#############################################################################################################

##
##


##

##    
window.mainloop()

#interface_set()


