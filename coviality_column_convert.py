import pandas as pd
import numpy as np

# MAKE SURE THIS IS CORRECT
df = pd.read_csv('data/covitality.csv')

def columns_to_values(row, df):
    for column in ['STRENGTHS', 'ENHANCE', 'GROWTH']:        
        if pd.isnull(row[column]) == False:
            _data = row[column].split(',')
            for indicator in _data:
                if indicator in list(df.columns):
                    row[indicator] = column
                else:
                    print('error')
    return row


columns_to_create = []
def create_columns(row):
    for column in ['STRENGTHS', 'ENHANCE', 'GROWTH']:        
        if pd.isnull(row[column]) == False:
            _data = row[column].split(',')
            for indicator in _data:
                if indicator not in columns_to_create:
                    columns_to_create.append(indicator)
    pass


_ = df.apply(lambda row: create_columns(row), axis=1)



for col in columns_to_create:
    df[col] = ""
    
column_order = list(df.columns)



df = df.apply(lambda row: columns_to_values(row, df), axis=1)


df = df.reindex(columns=column_order)


df.to_csv("data/covitality_results.csv", index=False)