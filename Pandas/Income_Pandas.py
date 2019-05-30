"""
Exploring the data using income.csv

@Author: Akshit Gupta
"""

#C:\Users\guptaksh.CORPDOM\Desktop\Self_Learning\MF_Python\Self_code\Pandas\Data\income.csv

#Importing pandas
import pandas as pd

#Importing Dataset
#To read or import data from CSV file, use read_csv() function
income = pd.read_csv("C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\income.csv")
type(income)

#Get Variable Names
#By using income.columnscommand
income.columns

#To view the dimensions or shape of the data
income.shape

#To view number of rows
income.shape[0]

#To view number of columns
income.shape[1]

#To get the infomration of the data types and the column name
income.info()

#To get the details like mean, max, min, std etc.
income.describe()

#returns first two column names 'Index', 'State'.
#indexing starts from 0. 
income.columns [:2]

#Knowing the Variable types
#use the dataFrameName.dtypes command to extract
#the information of types of variables stored in the data frame.
#'object' means strings or character variables.
#'int64' refers to numeric variables
income.dtypes

#To see the variable type of one variable
# 'O' refers to object i.e. type of variable as character.
income['Y2008'].dtypes
income.State.dtypes

#Changing the data types
#converts an integer into a float
income.Y2008 = income.Y2008.astype(float)
income.Y2008.dtypes

#To view only some of the rows
#head( ) shows first 5 rows
income.head()
income.head(2) #shows first 2 rows.

#tail( ) function shows last 5 rows
income.tail()
income.tail(2) #shows last 2 rows

#these can also select the first 5 rows
income [0:5]
income.iloc [0:5, :2] #Rows, Columns


"""
# Single selections using iloc and DataFrame
# Rows:
data.iloc[0] # first row of data frame
data.iloc[1] # second row of data frame
data.iloc[-1] # last row of data frame
# Columns:
data.iloc[:,0] # first column of data frame
data.iloc[:,1] # second column of data frame
data.iloc[:,-1] # last column of data frame
# Multiple row and column selections using iloc and DataFrame
data.iloc[0:5] # first five rows of dataframe
data.iloc[:, 0:2] # first two columns of data frame with all rows
data.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns
data.iloc[0:5, 5:8] # first 5 rows and 5th, 6th, 7th columns of data frame
"""

# Rows:
income.iloc[0] # first row of data frame
income.iloc[1] # second row of data frame
income.iloc[-1] # last row of data frame

# Columns:
income.iloc [:,0] # first column of data frame
income.iloc[:,1] # second column of data frame
income.iloc[:,-1] # last column of data frame

# Multiple row and column selections using iloc and DataFrame
income.iloc [:5] # first five rows of dataframe
income.iloc [:,:2] # first two columns of data frame with all rows
income.iloc[[0,3,6,24],[0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns
income.iloc [0:5,[4,5,6]] # first 5 rows and 5th, 6th, 7th columns of data frame

#nunique( ) shows the number of unique values.
income.Index.nunique()









