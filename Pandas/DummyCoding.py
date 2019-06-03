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

iris = pd.read_csv("C:\\Users\\guptaksh.CORPDOM\\Desktop\\Self_Learning\\MF_Python\\Self_code\\Pandas\\Data\\iris.csv")
type(iris)

#Creating of DataFrame using the pandas
akshit = pd.DataFrame({'Name': 'Akshit', 'Last': 'Gupta'})
akshit = {'Name': ['Akshit','Abhinav'], 'Last': 'Gupta'}
type(akshit)

akshit_df = pd.DataFrame(akshit)
akshit_df






