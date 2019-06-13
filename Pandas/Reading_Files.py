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

pd.read_csv('C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\titanic.csv', header=0)