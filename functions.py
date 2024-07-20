import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def inspect_dataframe_column(dataframe, column):
    dataframe[column].value_counts()
    print(dataframe[column].value_counts())
    percentage_of_missing = dataframe[column].isnull().mean() * 100
    print(f"Percentage missing: {percentage_of_missing}")



def plot_dataframe_missing_values(dataframe, filepath):
    # Gets the mean of missing values in each column. Since True = 1 and False = 0 the mean tells us how much of the data is missing.
    missing_values = dataframe.isnull().mean().sort_values(ascending=False)
    
    # Create the bar plot
    plt.figure(figsize=(12, 6))
    missing_plot = missing_values.plot(kind='bar')
    
    # Customize the plot
    plt.xlabel('Columns')
    plt.ylabel('Number of Missing Values')
    plt.title('Missing Value Ratio per Column (Sorted)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Show the plot
    plt.show()
    plt.savefig(filepath)