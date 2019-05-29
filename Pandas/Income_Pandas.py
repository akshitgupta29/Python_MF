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
income


