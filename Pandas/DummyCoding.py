"""
Introduction to Dummy Coding and Image Handling.
Images for reference for Dummy coding are opened in the code first.

@Author: Akshit Gupta
"""

#To open a image, use the following library
from PIL import Image
img1 = Image.open("C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Images\\Dummy_Coding_1.jpg").show()
img2 = Image.open("C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Images\\Dummy_Coding_1a.jpg").show()
img3 = Image.open("C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Images\\Dummy_Coding_1b.jpg").show()

import pandas as pd
import numpy as np 

#Creating of DataFrame using the pandas
akshit = pd.DataFrame({'Name': 'Akshit', 'Last': 'Gupta'})
akshit = {'Name': ['Akshit','Abhinav'], 'Last': 'Gupta'}
type(akshit)

akshit_df = pd.DataFrame(akshit)
akshit_df

iris = pd.read_csv("C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\iris.csv")

#Exploring the basic data
type(iris)
iris.head()
iris.tail()
iris.loc[:,"Sepal.Length"]
iris.Species.unique()

#map( ) function is used to match the values and replace
#them in the new series automatically created.
iris["setosa"] = iris.Species.map({'setosa':1, 'versicolor':0, 'virginica':0})
iris.head()
iris.tail()
iris.Species.unique()

#To create dummies get_dummies( ) is used. 
#iris.Species.prefix = "Species" adds a prefix ' Species' 
#to the new series created.

#selects the columns until (excluding) the first column
pd.get_dummies(iris.Species, prefix="Species").columns
pd.get_dummies(iris.Species, prefix="Species")

iris.head() #Doesn't change the original values as they doesn't exist.

#Will run, but give only one output as there is no categories present in the data.
pd.get_dummies("iris.Sepal.Length", prefix="Len")

pd.get_dummies(iris.Species, prefix="Species").iloc[:,0:1] #1 is not included. It will display all the values including those of zeros.
pd.get_dummies(iris.Species, prefix="Species").iloc[:,0]

special_dummies = pd.get_dummies(iris.Species, prefix="Species").iloc[:,0:]
type(special_dummies)

#With concat( ) function we can join multiple series or dataFrames. 
#axis = 1 denotes that they should be joined columnwise.
iris_concatenated = pd.concat([iris, special_dummies], axis=1)
iris_concatenated
iris_concatenated.columns

#Illogical to concatenate as the data will be absurd.
iris_concatenated_row = pd.concat([iris, special_dummies], sort=False)
iris_concatenated_row
iris_concatenated_row.columns

#It is usual that for a variable with 'n' categories we creat 'n-1' dummies, 
#thus to drop the first 'dummy' column we write drop_first = True
pd.get_dummies(iris, columns=["Species"], drop_first=True)
pd.get_dummies(iris, columns=["Species"], drop_first=True).columns

#Ranking
#Ranking by a specific variable
#to rank the Sepal.Length for different species in ascending order
#Using cumsum( ) function ONE can obtain the cumulative sum
iris['Rank'] = iris['Sepal.Length'].rank(ascending=True)
iris.columns
iris.head()














