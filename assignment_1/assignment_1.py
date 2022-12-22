# Assignment:
# You have to read the below CSV file and convert the data in json format given in the sample file

import pprint
import pandas as pd
import json

df = pd.read_csv(r'mvf_user.csv')
groupby_dataframe = df.groupby(['user_id','email_id']).apply(lambda x: x.to_json(indent = 0 ,orient='records')).reset_index().rename(columns={0:'multi_records'})
print(groupby_dataframe)
convert_json = json.loads(groupby_dataframe.to_json(orient='records'))
with open('groupby_dataframe.json', 'w') as f:
    count = 0
    f.write("{")
    f.write('"data":[')
    f.write("{")
    for obj in convert_json:
        obj["multi_records"] = json.loads(obj["multi_records"])
        json.dump(obj, f, indent=4)
        count=count+1
        #print(count)
        if count<=42:
           f.write(",")
    f.write("]")
    f.write("}")
    f.close()