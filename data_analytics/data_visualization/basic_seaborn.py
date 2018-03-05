import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib


def corr_heatmap_with_values(df):
    corr = df.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(figsize=(17,15))
    cmap = sns.color_palette('coolwarm')
    sns.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5,
                yticklabels=True, annot=True, fmt='.2f', cbar_kws={'shrink':.5})
    plt.title('Correlation Matrix', fontsize=20)
    plt.xticks(rotation=90, fontsize=11)
    plt.yticks(rotation=0, fontsize=11)
    plt.tight_layout()

def data_and_regression_model_mean(df, group_by, x, y, titel):
    '''original:
    # Create new DataFrame with data grouped by team
    team_grouped = df.groupby('Team').mean()
    # Plot
    sns.lmplot(x='Points', y='Offensive_Rebounds', data=team_grouped, size=8)
    plt.title('Relationship Between Team Offensive Rebounding and Team Points', fontsize=15)'''
    # Create new DataFrame with data grouped by team
    grouped = df.groupby(group_by).mean()
    # Plot
    sns.lmplot(x=x, y=y, data=grouped, size=8)
    plt.title(titel, fontsize=15)
