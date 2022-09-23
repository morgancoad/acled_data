import pandas as pd

def column_filter(df, col, value):
    '''
    Returns a new dataframe from a given column in the dataframe 
    where each row contains the inputted value at inputted column
    '''
    updated_df1 = df.loc[df[col] == value]
    return updated_df1

def concat_mult_df(df):
    '''
    Concatenates two dfs
    '''
    concat_dfs = pd.concat([df1, df2])
    return concat_dfs

def top_twenty(df, col):
    '''
    Indenifies top twenty based on adding 
    how many times a string is repeated in a given column
    '''
    top_20 = df.value_counts(col).head(20)
    return top_20

def bottom_twenty(df, col):
    '''
    Indenifies bottom twenty based on adding 
    how many times a string is repeated in a given column
    '''
    bottom_20 = df.value_counts(col).tail(20)
    return bottom_20


def bottom_twenty_greater_one(df, col):
    '''
    Indenifies bottom twenty based on adding 
    how many times a string is repeated in a given column
    '''
    bottom_20_greater_one = df[(df[col] > 1)]
    return bottom_20_greater_one

def one_year(df, col, start, end):
    '''
    Filters data to one year with the end date one 
    day prior than the start date.
    '''
    df_one_year = df[(df[col] > start) & (df[col] <= end)]
    return df_one_year





if __name__ == '__main__':
    df = pd.read_csv('../data/acled_midterm.csv')
   