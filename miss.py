import pandas as pd 
import numpy as np 
data={
    'First_Score':[20,30,np.nan,40],
    'Second_Score':[20,np.nan,30,40],
    'Third_Score':[20,30,np.nan,40],
    'Fourth_Score':[20,30,40,np.nan]
}
print(data)
df=pd.DataFrame(data)
#checking missing values
print(df.isnull().sum())
#checking which are not missing values
print(df.notnull())
#fillna
print(df.fillna(50))
#filling with mean 
df['Second_Score']=df['Second_Score'].fillna(df['Second_Score'].mean())
#filling with median
df['Second_Score']=df['Second_Score'].fillna(df['Second_Score'].median())
#flling with mode
df['Second_Score']=df['Second_Score'].fillna(df['Second_Score'].mode())
#dropna
print(df.dropna())
#dropping column 
print(df.dropna(axis=0))
#dropping row
print(df.dropna(axis=1))
