"""
Reading the different formats of files.
Exploring the various arguments present under the read functions().

@Author: Akshit Gupta
"""

import pandas as pd
import numpy as np

pd.read_csv('C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\titanic.csv')

#Taking the index column as pclass.
pd.read_csv('C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\titanic.csv', index_col='pclass')

