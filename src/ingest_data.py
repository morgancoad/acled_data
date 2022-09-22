import pandas as pd

def to_datetime(df,col):
    '''
    converts col to datetime. 
    adds new cols of month and year
    ARGS:
        df = dataframe
        col = str
    RETURN
        df
    '''
    df[col] = pd.to_datetime(df[col])
    df['month'] = pd.DatetimeIndex(df[col]).month_name().str[:3]
    df['year'] = pd.DatetimeIndex(df[col]).year
    return df






if __name__ == '__main__':
    df1 = pd.read_csv('../data/owid-covid-data.csv')
    df2 = pd.read_csv('../data/acled_midterm.csv')
    # print(df.info())
    df1 = to_datetime(df, 'date')
    # print(df1.info())