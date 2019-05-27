"""
#Pandas are well suited for tabular data with heterogeneously typed columns, as in an
#SQL table or Excel spreadsheet.

#Data Structure

#sPandas introduces two new data structures to Python – Series and DataFrameCreating a pandas series
# creating a series by passing a list of values, and a custom index label.
#Note that the labeled index reference for each row and it can have duplicate
#values

"""

import numpy as np
import pandas as pd

s = pd.Series ([1,2,3,np.nan, 5,6], index = ['a', 'b', 'c','c', 'e', 'f'])

print (s)

#Creating a pandas dataframe
data = {'Gender': ['F', 'M', 'M'], 'Emp_ID' : ['E01', 'E02', 'E03'], 'Age' : [25,26,27]}

print (data)

# We want the order the columns, so lets specify in columns parameter
df = pd.DataFrame (data, columns = ['Emp_ID', 'Gender', 'Age'])
print (df)
df



