"""
Reading the different formats of files.
Exploring the various arguments present under the read functions().

@Author: Akshit Gupta
"""

import pandas as pd
import numpy as np

titanic = pd.read_csv('C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\titanic.csv')
titanic

#Taking the index column as pclass.
pd.read_csv('C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\titanic.csv', index_col='pclass')

#To make the second row of a csv file as a header. By default the first row is treated as header.
pd.read_csv('C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\titanic.csv', header=1)

#To have no header and taking the first row in csv as the first row only.
pd.read_csv('C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\titanic.csv', header=None)

#To show the columns in the order supplied.
pd.read_csv('C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\titanic.csv', header=0, names=["alive","class","gender", "age","sibsp","parch","price","emb","deck"])

#Don't try this. Fully distorted.
pd.read_csv('C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\titanic.csv', header=0, names=["alive","class","gender", "age","sibsp","parch"])

#To use only specific columns from the csv.
pd.read_csv('C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\titanic.csv', header=0, usecols=["survived", "pclass", "sex", "age"])


