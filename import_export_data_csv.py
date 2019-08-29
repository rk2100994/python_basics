import pandas as pd

#Importing data into pandas dataframe from csv
d = pd.read_csv('pandas_dataset.csv')
print(d)

#Exporting data into csv from pandas dataframe
data = {"Sox":pd.Series([50,40,60],index=["maths","science","social"]),
"Fox": pd.Series([60,30,70], index=["maths","science","social"])}
df=pd.DataFrame(data)
df.to_csv('pandas_dataset_to.csv')

