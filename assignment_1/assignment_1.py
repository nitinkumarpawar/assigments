# Assignment:
# You have to read the below CSV file and convert the data in json format given in the sample file

import pandas as pd

df = pd.read_csv(r'mvf_user.csv')
convert_json = df.to_json(r'converted_mvf_user.json')
json_output = df.to_json(convert_json, indent=1, orient='records')
print(json_output)
