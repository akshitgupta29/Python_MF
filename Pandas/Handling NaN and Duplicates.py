"""
Handling NaN values and duplicate values in the data.

@Author: Akshit Gupta
"""

#missing values
#create a new dataframe named 'crops' 
#create a NaN value by using np.nan by importing numpy.

import numpy as np
import pandas as pd

mydata = {'Crop': ["Rice", 'Wheat', 'Barley', 'Maize'], 'Yeild':[1010, 1025.2,1404.2,1251.7], 'cost':[102,np.nan, 20, 68]}
mydata
type(mydata) #Dictionary

crops = pd.DataFrame(mydata)
type(crops) #Pandas Data Frame
crops

#isnull( ) returns True 
#notnull( ) returns False if the value is NaN.
crops.isnull()
crops.notnull()
crops.isnull().sum()
crops.notnull().sum()

#crops.cost.isnull() firstly subsets the 'cost' from 
#the dataframe and returns a logical vector with isnull()
crops[crops.cost.isnull()] #shows the rows with NAs.
crops[crops.cost.isnull()].Crop #shows the rows with NAs in crops.Crop
crops[crops.cost.notnull()].Crop #shows the rows without NAs in crops.Crop

#To remove NaNs if any of 'Yield' or'cost' are missing
#use the subset parameter and pass a list:
a = crops.dropna()
