import pandas as pd

url = '/Users/khalilur/Documents/Python/PythonMachineLearningCookBook/LoadingData/loadingCSV_EXCEL_JSON_SQL/data_titanic.json'

dataframe = pd.read_json(url, orient='columns')

print(dataframe.head(0))