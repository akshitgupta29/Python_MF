import pandas as pd
import numpy as np


"""
#Pandas are well suited for tabular data with heterogeneously typed columns, as in an
#SQL table or Excel spreadsheet.

#Data Structure

#sPandas introduces two new data structures to Python – Series and DataFrameCreating a pandas series
# creating a series by passing a list of values, and a custom index label.
#Note that the labeled index reference for each row and it can have duplicate
#values

"""

s = pd.Series ([1,2,3,np.nan, 5,6], index = ['a', 'b', 'c','c', 'e', 'f'])

print (s)

#Creating a pandas dataframe
data = {'Gender': ['F', 'M', 'M'], 'Emp_ID' : ['E01', 'E02', 'E03'], 'Age' : [25,26,27]}

print (data)

# We want the order the columns, so lets specify in columns parameter
df = pd.DataFrame (data, columns = ['Emp_ID', 'Gender', 'Age'])
print (df)
df

#Concat or append operation
data = {
'emp_id': ['1', '2', '3', '4', '5'],
'first_name': ['Jason', 'Andy', 'Allen', 'Alice', 'Amy'],
'last_name': ['Larkin', 'Jacob', 'A', 'AA', 'Jackson']}
df_1 = pd.DataFrame(data, columns = ['emp_id', 'first_name', 'last_name'])
data = {
'emp_id': ['4', '5', '6', '7'],
'first_name': ['Brian', 'Shize', 'Kim', 'Jose'],
'last_name': ['Alexander', 'Suma', 'Mike', 'G']}
df_2 = pd.DataFrame(data, columns = ['emp_id', 'first_name', 'last_name'])

df_1
df_2

# Usingconcat
df = pd.concat([df_1, df_2])
df
#The other way
df_1.append(df_2)

#Concatenation on the basis of columns
pd.concat([df_1, df_2], axis=1)

#Merge two dataframes
# Merge two dataframes based on the emp_id value
# in this case only the emp_id's present in both table will be joined
pd.merge(df_1,df_2, on='emp_id')

#Join
"""
Pandas offer SQL style merges as well.
Left join produces a complete set of records from Table A, with the matching records
where available in Table B. If there is no match, the right side will contain null.
"""

#Left join two dataframes
# Left join
pd.merge(df_1, df_2, on='emp_id', how='left')
# Merge while adding a suffix to duplicate column names of both table
print(pd.merge(df_1, df_2, on='emp_id', how='left', suffixes=('_left', '_right')))


"""
Right join - Right join produces a complete set of records from Table B,
with the matching records where available in Table A. If there is no match,
the left side will contain null.
"""

# Right join
print(pd.merge(df_1, df_2, on='emp_id', how='right'))

"""
Inner Join - Inner join produces only the set of records that match in both Table A
and Table B.
"""
print(pd.merge(df_1, df_2, on='emp_id', how='inner'))


"""
Outer Join - Full outer join produces the set of all records in Table A and Table B, with
matching records from both sides where available. If there is no match, the missing side
will contain null
"""
print(pd.merge(df_1, df_2, on='emp_id', how='outer'))

