import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def describeColumn(columnname, df, title = ''):
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax = ax.flatten()
    value_counts = df[columnname].value_counts()
    labels = value_counts.index.tolist()
    colors =["#4caba4", "#d68c78",'#a3a2a2','#ab90a0', '#e6daa3', '#6782a8', '#8ea677']
    
    # Donut Chart
    wedges, texts, autotexts = ax[0].pie(
        value_counts, autopct='%1.1f%%',textprops={'size': 9, 'color': 'white','fontweight':'bold' }, colors=colors,
        wedgeprops=dict(width=0.35),  startangle=80,   pctdistance=0.85  )
    # circle
    centre_circle = plt.Circle((0, 0), 0.6, fc='white')
    ax[0].add_artist(centre_circle)
    
    # Count Plot
    sns.countplot(data=df, y=columnname, ax=ax[1], palette=colors, order=labels)
    for i, v in enumerate(value_counts):
        ax[1].text(v + 1, i, str(v), color='black',fontsize=10, va='center')
    sns.despine(left=True, bottom=True)
    plt.yticks(fontsize=9,color='black')
    ax[1].set_ylabel(None)
    plt.xlabel("")
    plt.xticks([])
    fig.suptitle(title if title else columnname, fontsize=15, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.show()

def summary(df):
    summ = pd.DataFrame(df.dtypes, columns=['data type'])
    summ['#missing'] = df.isnull().sum().values
    summ['Duplicate'] = df.duplicated().sum()
    summ['#unique'] = df.nunique().values
    desc = pd.DataFrame(df.describe(include='all').transpose())
    summ['min'] = desc['min'].values
    summ['max'] = desc['max'].values
    summ['avg'] = desc['mean'].values
    summ['std dev'] = desc['std'].values
    summ['top value'] = desc['top'].values
    summ['Freq'] = desc['freq'].values

    return summ

# Checking for distributions
def dist(df1, columns_list, rows, cols, df2 = pd.DataFrame):
    fig, axs = plt.subplots(rows, cols, figsize=(24, 10))
    axs = axs.flatten()
    
    for i, col in enumerate(columns_list):
        sns.kdeplot(df1[col], ax=axs[i], fill=True, alpha=0.5, linewidth=0.5, color='#05b0a3', label='df1')
        if not df2.empty:
            sns.kdeplot(df2[col], ax=axs[i], fill=True, alpha=0.5, linewidth=0.5, color='#d68c78', label='df2')
        # axs[i].set_title(f'{col}, df1 skewness: {df1[col].skew():.2f}{f', df2 skewness: {df2[col].skew():.2f}' if df2 != None else ''}')
        axs[i].legend()
        
    plt.tight_layout()