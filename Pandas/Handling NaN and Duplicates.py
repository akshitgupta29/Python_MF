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
a = crops.dropna(subset=['Yeild','cost'], how='any')
a
crops
b = crops.dropna()
b
c = crops.dropna(subset=["Yeild",'cost'], how='all')
c

#Dealing with duplicates
data = pd.DataFrame({"Items" : ["TV","Washing Machine","Mobile","TV","TV","Washing Machine"], 
                     "Price" : [10000,50000,20000,10000,10000,40000]})
data
data2 = data.copy()
data2

"""
pandas.DataFrame.duplicated

Return boolean Series denoting duplicate rows, optionally only considering certain columns.
Parameters:	
subset : column label or sequence of labels, optional
Only consider certain columns for identifying duplicates, by default use all of the columns

keep : {‘first’, ‘last’, False}, default ‘first’
first : Mark duplicates as True except for the first occurrence.
last : Mark duplicates as True except for the last occurrence.
False : Mark all duplicates as True.

Returns:	
duplicated : Series

"""

#duplicated() returns a logical vector returning True 
#when encounters duplicated.
data.duplicated()
data.duplicated().sum() #number of duplicatees in the data.
data.loc[data.duplicated(),:]

#By default keep = 'first' i.e. the first occurence is considered a unique 
#value and its repetitions are considered as duplicates.
#If keep = "last" the last occurence is considered a unique value 
#and all its repetitions are considered as duplicates.

#last entries are not there,indices have changed.
data.loc[data.duplicated(keep="last"),:]

#If keep = "False" then it considers all the occurences of the repeated 
#observations as duplicates.

#all the duplicates, including unique are shown.
data.loc[data.duplicated(keep=False)]

#To drop the duplicates drop_duplicates is used 
#with default inplace = False, keep = 'first' or 'last' 
#or 'False' have the respective meanings as in duplicated( )
data.drop_duplicates(keep = "first")
data.drop_duplicates(keep = "last")
data.drop_duplicates(keep=False, inplace=True) #by default inplace = False
data
data2.drop_duplicates(keep=False)
data2




