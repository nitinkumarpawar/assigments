# Assignment: 
# You have to read the below CSV file and convert the data in json format given in the sample file

import csv
from flask import jsonify
import pandas as pd
import json
from collections import defaultdict
import re

df = pd.read_csv(r'mvf_user.csv')
df.to_json(r'converted_mvf_user.json')
df1 = pd.read_json('converted_mvf_user.json')
# df_inner = pd.merge(df1,df1, how = 'inner', left_on=['id', 'status_hash'], right_on=['id', 'firstname'])
df_inner = pd.DataFrame(df1)
print(df_inner)
df_inner.to_json("new.json")










