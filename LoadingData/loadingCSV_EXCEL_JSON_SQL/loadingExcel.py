import pandas as pd

url = '/Users/khalilur/Documents/Python/PythonMachineLearningCookBook/LoadingData/loadingCSV_EXCEL_JSON_SQL/titanic3.xls'

dataframe = pd.read_excel(url,sheet_name=0, header=1)

print(dataframe.head(0))