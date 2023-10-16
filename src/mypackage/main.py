import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime



# Créer une colonne time_s pour déterminer la diff en second entre la ligne current et la première ligne 
def get_time_diff(df):
    df['date'] = pd.to_datetime(df['TIMESTAMP'], unit='s')
    start_date = df['date'].iloc[0]
    df['time_s'] = (df['date'] - start_date).dt.total_seconds()

# Reduce the size of the dataFrame by removing duplicate rows
def remove_duplicates(df, signaux):
    df.drop_duplicates(subset = signaux, keep = 'first', inplace= True)

#function to merge between two dfs based on their timestamp
def merge_df(df1,df2):
    # this is a merge function 
    # Concatenate df1 and df2
    merged_df = pd.concat([df1, df2], ignore_index=True)
    # Sort the DataFrame by 'TIMESTAMP' column
    merged_df.sort_values('TIMESTAMP', inplace=True)
    merged_df.interpolate(inplace=True)
    return merged_df