print ("This is the database.py file")#starting module called main module
print("Python thinks this is called {}".format(__name__))

# import blood_calculator as bc #the best way
# from blood_calculator import HDL_analysis,generic_input
from blood_calculator import total_analysis 
from other_module import *  #import everything blood_calculator
# import numpy as np


HDL = 55


HDL_analysis =  HDL_analysis(HDL)

print("The HDL analysis is {}".format(HDL_analysis))

generic_input("Other Test") #don't know where generic_input comes from 
print(LDL_analysis(13))