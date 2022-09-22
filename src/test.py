import pandas as pd
import numpy as np

# def column_filter(df, col, value):
#     '''
#     Returns a new dataframe from a given column in the dataframe 
#     where each row contains the inputted value at inputted column
#     '''
#     updated_df1 = df.loc[df[col] == value]
#     return updated_df1

# def concat_mult_df(df):
#     '''
#     Concatenates two dfs
#     '''
#     concat_dfs = pd.concat([df1, df2])
#     return concat_dfs

def top_twenty(df1, col):
    '''
    Indenifies top twenty based on adding 
    how many times a string is repeated in a given column
    '''
    top_20 = df1.value_counts('col').head(20)
    return top_20


if __name__ == '__main__':
    df = pd.read_csv('../data/acled_midterm.csv')
    # print(df.info())
    df = top_twenty('acled_event_protests', 'actor1')
    print(df)
  