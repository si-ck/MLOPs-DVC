import pandas as pd
import os 

data = {"name":['sik','rahul','karan'],
        "age":[20,19,19],
        "city" : ['hyd','pjb','assam']}

df = pd.DataFrame(data)
##add data 

new0 = {'name':"arjun",
        'age':20}
#df.loc[len(df)] = new0
## add more data
new1 = {"name":"varun",
        "age":19,
        "city":"hyd"}
df.loc[len(df)] = new1

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, "sample_data.csv")
df.to_csv(file_path, index=False)





print(f"CSV file has ben saved to {file_path}")