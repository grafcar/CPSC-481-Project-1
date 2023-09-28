import pandas as pd

#Load spreadsheet
xl = pd.ExcelFile('data.xlsx')

#Load a sheet into a DataFrame by its name
df = xl.parse('Sheet1')

#Select columns for the first sub-dictionary
sub_dict1 = df[['Name', 'Units']].to_dict()

#Select columns for the second sub-dictionary
sub_dict2 = df[['Name', 'Prereq']].to_dict()

#Combine the sub-dictionaries into one dictionary
dict_data = {'SubDict1': sub_dict1, 'SubDict2': sub_dict2}

print(dict_data)