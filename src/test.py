import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib import dates as mpl_dates
import matplotlib.dates as mdates
import plotly.express as px
import plotly.graph_objects as go
import os

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




# def top_twenty(df, col):
#     '''
#     Indenifies top twenty based on adding 
#     how many times a string is repeated in a given column
#     '''
#     top_20 = df.value_counts(col).head(20)
#     return top_20



def bargraph_top_twenty(df):
    '''
    Receives df and makes bar graph.
    '''
    bar_graph = fig, ax = plt.subplots(figsize=(12,9))
    ax.bar(df.index, df)
    ax.set_xticklabels(df.index, rotation=90, horizontalalignment = 'right', fontsize = '12')
    plt.show()
    return bar_graph




if __name__ == '__main__':
    df = pd.read_csv('../data/acled_midterm.csv')
    # print(df.info())
    df = bargraph_top_twenty(df)
    print(df)
  