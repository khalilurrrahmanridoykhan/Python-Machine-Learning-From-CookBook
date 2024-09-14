import pandas as pd
url = '/Users/khalilur/Documents/Python/PythonMachineLearningCookBook/LoadingData/loadingCSV_EXCEL_JSON_SQL/titanic.csv'

datafram = pd.read_csv(url)

print(datafram.head(2))