import pandas as pd

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
    top_20 = df1['col'].value_counts().head(20)
    return top_20
