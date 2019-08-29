import pandas as pd 
import numpy as np
#Series is 1D

arr = np.array([20,1,357,23,6])

series = pd.Series(arr)
print(series)
#accessing by sllicing
print("Slicing",series[1:3])

data_dict = {'a':1,'b':2,'c':3}
print(pd.Series(data_dict))


data_lx = [{0:'hi',1:"hello",2:"hru"},{0:'namastey',1:'namaskaram',2:'aadaab'},{0:'bye',1:'goodbye'}]
table = pd.DataFrame(data_lx)
print(table)

#To give specific column names, if nothing given we get by default values as 0,1,2....
data_lx = [{0:'hi',1:"hello",2:"hru"},{0:'namastey',1:'namaskaram',2:'aadaab'},{0:'bye',1:'goodbye'}]
table = pd.DataFrame(data_lx, index = ["row1","row2","row3"])
print(table)

#Data Frame using Series
marks_series1 = pd.Series([50,40,60],index=["maths","science","social"])
marks_series2 = pd.Series([60,30,70], index=["maths","science","social"])
# print(marks_series1)
# print(marks_series2)
table=pd.DataFrame({
	'Jim':marks_series1,
	'Jam':marks_series2
})
print(table)
# print(type(table))

#Another type
data = {"Sox":pd.Series([50,40,60],index=["maths","science","social"]),
"Fox": pd.Series([60,30,70], index=["maths","science","social"])}
# print(marks_series1)
# print(marks_series2)
df=pd.DataFrame(data)
print(df)
'''
To add column to existing dataframe, here order of 
index is not followed as above indexes still, 
the values assigned in order."english is not added as its not present for above data"
'''

df['Mox'] = pd.Series([60,70,90,100],index=["maths","social","science","english"])
print(df) 
#This completly destroys it, it does not return anythin'
del(df['Sox'])
print(df)
#But to return something and remove we need to use pop
df['Pox'] = pd.Series([20,30,50],index=["maths","social","science"])
print(df)
pox_series = df.pop('Pox')
print(pox_series)
print(df)
#to select data rows method1
print(df.loc['maths'])
#to select data rows method2,iloc is integer location
print(df.iloc[1])
#To append row
df = df.append(pd.DataFrame([[45,65]],columns=["Fox","Mox"]))
print(df)
indexNamesArr = df.index.values
print("row index values",indexNamesArr)
indexNamesArr[3]="english"
print("row index values",indexNamesArr)
print("type of index values",type(indexNamesArr))
columnsNamesArr = df.columns.values
print("columns index values",columnsNamesArr)

# drop columns
df = df.drop('maths')
print(df)
