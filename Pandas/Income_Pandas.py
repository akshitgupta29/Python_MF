"""
Exploring the data using income.csv
Exploring includes going thorugh the data, retrieve specific columns, rows, use group by and filters in the code.

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

#Extract Unique Values
#shows the unique levels or categories in the dataset.
income.Index.unique()

#Cross Tab
#pd.crosstab( ) is used to create a frequency distribution
pd.crosstab(income.Index, income.State)

#Creating a frequency distribution

#income.Index selects the 'Index' column 
#and value_counts( ) creates a frequency distribution.
income.Index.value_counts(ascending=True)
income.Index.value_counts() #Bydefault = False

# draw the samples
#income.sample( ) is used to draw random samples 
#from the dataset containing all the columns.
# frac = 0.1 tells that we need 10 percent of the data as my sample.
income.sample (frac=0.1)

#Selecting columns
#use either loc[ ] or iloc[ ] 
#loc requires the column(rows) names to be selected
#while iloc requires the column(rows) indices (position).

# both Index and Y2008 are included.
income.loc[:, ['Index', 'Y2008']]

#Selecting consecutive columns
income.loc [:, 'Y2002':'Y2008']

#Columns from 1 to 5 are included. 6th column not included
income.iloc[:,0:5]

#Columns, Rows from 1 to 5 are included. 6th column not included
income.iloc [0:5,0:5]

#This can also select specific variables.
income[["Index", "Y2002"]]

#Create new variables
#Using eval( ) arithmetic operations columns can be done
income["difference"] = income.Y2008 - income.Y2009
income["difference"]

income.shape
#Alternatively
income["difference2"] = income.eval('Y2008-Y2009')
income["difference2"]
income.loc[:,"difference2"]
income.loc[0:5,"difference2"] 
income.head()
income.columns
data = income.assign(ratio=(income.Y2008/income.Y2009))
data.head() #Changed
income.columns #Columns are not changed
data.columns

#Descriptive Statistics
income.describe() #for numeric variables

#To find the total count, maximum occuring string and its frequency we write include = ['object']
income.describe (include = 'object') #Only for strings / objects
income.describe(include = ['object'])

income.Y2008.mean()
income.Y2008.max()
income.Y2008.min()
income.Y2008.median()
income.loc[:,['Y2002', 'Y2008']].min()
income.loc[:,['Y2002', 'Y2008']].max()

#Groupby function
#To group the data by a categorical variable use groupby( ) function 
income.groupby("Index").Y2008.min()
income.groupby("Index")["Y2008", "Y2010"].max()

#agg( ) function is used to find all the functions for a given variable.
income.groupby("Index").Y2002.agg(["count", 'min', 'max', 'mean'])
income.groupby("Index")['Y2002','Y2008'].agg(['min','max', 'count', 'mean', 'median'])

#finds minimum and maximum values for Y2002 and only mean for Y2003
income.groupby("Index").agg({'Y2002':['min','max'], 'Y2003':'mean'})

#Filtering
#To filter only those rows which have Index as "A" 
income[income.Index=='A']
income.loc[income.Index=='A', :]

#To select the States having Index as "A":
income.loc[income.Index=='A',"State"]
income.loc [(income.Index=='A') & (income.State == 'Alaska')]

#To filter the rows with Index as "A" and income for 2002 > 1500000"
income.loc[(income.Index=='A') & (income.Y2002>1500000)]

#To filter the rows with Index as "A" or income for 2002 > 1500000"
income.loc[(income.Index=='A') | (income.Y2002 > 1500000),:]

#To filter the rows with Index as "A" or income for 2002 > 1500000" and display these two columns only
income.loc[(income.Index=='A') | (income.Y2002 > 1500000), ['Index', 'Y2002']]

#To filter the rows with index either "A" or "W", we can use isin( ) function:
income.loc[(income.Index == 'A') | (income.Index == 'W'), :]
income.isin(['A', 'W'])

#To get the number of values of True, False in the given data set and to use it to get the total number of data.
income.isin(['A', 'W']).loc[:,["Index","State"]].sum()