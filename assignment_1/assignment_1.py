# Assignment:
# You have to read the below CSV file and convert the data in json format given in the sample file

import csv
import pandas as pd
import json

df = pd.read_csv(r'mvf_user.csv')
df.to_json(r'converted_mvf_user.json')

read_json = open(
    '/Users/nitinkumarpawar/Developer/Arrk/Training/assignments/assignment_1/converted_mvf_user.json', 'r')

json_data = read_json.read()
json_obj = json.loads(str(json_data))

json_to_dic = json.load(json_data)
print(json_to_dic)
print(type(json_to_dic))

read_json.close()
