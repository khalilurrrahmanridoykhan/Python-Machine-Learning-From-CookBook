import pandas as pd

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
print(repalceregularexpressions)

