import pandas as pd

dataframe = pd.DataFrame()

dataframe['Name'] = ['Ridoy khan', 'Rana Khan', 'Fahmida Jannat']
dataframe['Age'] = [24, 21, 24]
dataframe['Driver'] = [True, False, True]

# Append A new row At Bottom 
new_row = pd.Series(
[
    'Dhrubo', 23, True,
],
index=['Name', 'Age', 'Driver']
)


print(dataframe)