import pandas as pd
import numpy as np
url = '/Users/khalilur/Documents/Python/PythonMachineLearningCookBook/DataWrangling/titanic.csv'
dataframe = pd.read_csv(url)

shape = dataframe.shape
decribe = dataframe.describe()

# Navigating DataFrames
find_first_row = dataframe.iloc[0]

firt_four_rows = dataframe.iloc[0:4]
another_way_find_first_four_rows = dataframe.iloc[:4]
dataframeforSurvived = dataframe.set_index(dataframe['survived'])
find_row_with_index = dataframe.loc[0]

selectsex = dataframe[(dataframe['sex'] == 'female') & (dataframe['survived'] == 1) & (dataframe['age'] >= 60.0)]
# (Row * Column)
quary = selectsex.shape

# Replace The Value
replacefemale = dataframe['sex'].replace("female", "Woman")
replacefemalandmaleboth = dataframe['sex'].replace(["female", "male"], ["male", "female"]).head(5)
repaleaSingledatainwhaledataset = dataframe.replace(0, "Replaced").head(2)
repalceregularexpressions = dataframe.replace(r"First", "1st",regex=True).head(10)

# Rename Column 
renamecolumn = dataframe.rename(columns={'sex': 'Gender', 'fare': 'Remane1'}).head(2)
# max, min, sum, ave count
max = dataframe['age'].max()
min = dataframe['age'].min()
sum = dataframe['age'].sum()
count = dataframe['age'].count()
dataframcount = dataframe.count()
# unique Value
uniquesex = dataframe['sex'].unique()
valuecount = dataframe['sex'].value_counts()
nonuniq = dataframe['age'].nunique()
# Handling Missing Value
missingvalue = dataframe[dataframe['age'].isnull()]
missingvaluesex = dataframe['sex'].replace('male',np.nan)
# Deleting a column
deleteclumn = dataframe.drop('age', axis=1).head(2)
deletecolumnmore = dataframe.drop(['class', 'sex'], axis=1).head(2)
deletecolumwithoutname = dataframe.drop(dataframe.columns[1], axis=1).head(2)
# Deleting a row
deleterow = dataframe[dataframe['sex'] != 'male'].head(2)
# Deleting a row with value
deleterowwithvalue = dataframe[dataframe.index != 0].head(2)
# Drop Duplicate rows
dropduplicate = dataframe.drop_duplicates()
dropsuplicatewithkeep = dataframe.drop_duplicates(subset=['sex'], keep='last')
#  Grouping Rows by Values
grouprow = dataframe.groupby('survived')['sex'].count()
grouprowbyname= dataframe.groupby(['sex', 'survived'])['age'].count()
# Looping Over THe Column
# for sex in dataframe['sex'][0:10]:
#     print(sex.upper())
# Looping with list comperehensions 
loopingwithlistcomerehensions = [who.upper() for who in dataframe['who'][0:10]]
# Appling funcion over all elemnets in a column
def uppercase(x):
    return x.upper();
finduppercase = dataframe['who'].apply(uppercase)[0:10]
# Applying a function to groups
fucntiontogrp = dataframe.groupby('sex').apply(lambda x:x.count())
# concaternate two dataframe 
# concaternate = pd.concat(dataframe, dataframe, axis=1)
# merging datafram
mergingdataframe = pd.merge(dataframe, dataframe, on='survived')
print(mergingdataframe)

