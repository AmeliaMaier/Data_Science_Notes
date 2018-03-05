import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

def percent_values_null(df):
    percent_nulls = df.isnull().sum()/df.shape[0]
    print(percent_nulls.sort_values(ascending=False))

def impute_mean_for_null(df, null_columns, group_by):
    # null columns are the columns in the df that you will fill based on averages from others in the same group (defined by group_by list)
    # Calculate average values for each position/season combination
    impute_values = df.groupby(group_by).transform(lambda x: x.fillna(x.mean()))[null_columns]
    # Add those impute_values back into original DataFrame
    df[null_columns] = impute_values
    return df
    ''' original:
        I chose to impute the mean value for each field based on the player's position and corresponding season (i.e., if the player is a Center and has a null value in the 3_Point_% field for the 2016 season, I imputed the mean 3_Point_% for all Centers during the 2016 season.
    # Create list of columns possessing null values
    null_columns = ['3_Point_%', 'Free_Throw_%', '2_Point_%', 'Field_Goal_%', 'effective_Field_Goal_%']
    # Calculate average values for each position/season combination
    impute_values = df.groupby(['Position', 'Season']).transform(lambda x: x.fillna(x.mean()))[null_columns]
    # Add those impute_values back into original DataFrame
    df[null_columns] = impute_values'''
