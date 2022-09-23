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
    df = pd.read_csv('../data/owid-covid-data.csv')
  