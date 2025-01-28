import pandas as pd
import os 

data = {"name":['sik','rahul','karan'],
        "age":[20,19,19],
        "city" : ['hyd','pjb','assam']}

df = pd.DataFrame(data)
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, "sample_data.csv")
df.to_csv(file_path, index=False)

print(f"CSV file has ben saved to {file_path}")