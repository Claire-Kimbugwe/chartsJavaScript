import pandas as pd
from flask import request, session

df = pd.read_csv("pop_cities.csv")
df = df.drop(['Unnamed: 0', 'Unnamed: 0.1','zip_code'],axis =1 )

def column_names():
    # takes in nothing and returns a list of column names
    
    cols = df.columns.tolist() #make list 
    return cols

def x_features():
     #drop the price column and return a list of remaining columns

    return df.drop('sale_price', axis =1 ).columns

def beds():
    bed = df.num_bedrooms
    bed = beds.tolist()
    return bed 

print(type(beds()))