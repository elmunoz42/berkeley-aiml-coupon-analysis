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

def calculate_percentage_difference(value1, value2):
    """
    Calculate the percentage difference between two values using NumPy.
    
    Args:
    value1 (float): First value
    value2 (float): Second value
    
    Returns:
    float: Percentage difference between the two values
    """
    return np.abs(value1 - value2) / np.mean([value1, value2]) * 100

def calculate_percentage_change(original_value, new_value):
    """
    Calculate the percentage change between two values using NumPy.
    
    Args:
    original_value (float): The original value
    new_value (float): The new value
    
    Returns:
    float: Percentage change from the original value to the new value
    """
    return (new_value - original_value) / original_value * 100

def create_comparison_plot(data, conditions, title, note, filename, x_label='Acceptance Rate (COUPON_SUCCESS)', y_label='User Type', colors=["#FF9900", "#146EB4"]):
    """
    Create a comparison plot based on given conditions.
    
    Parameters:
    data (pd.DataFrame): The dataframe containing the data
    conditions (list): A list of two conditions for querying the dataframe
    title (str): The title of the plot
    note (str): Additional note to be added below the plot
    filename (str): Name of the file to save the plot
    x_label (str): Label for x-axis (default: 'Acceptance Rate (COUPON_SUCCESS)')
    y_label (str): Label for y-axis (default: 'User Type')
    colors (list): List of two colors for the bars (default: ["#FF9900", "#146EB4"])
    """
    # Query the dataframe to extract means based on conditions
    success_rate_1 = data.query(conditions[0])[['COUPON_SUCCESS']].mean().values[0]
    success_rate_2 = data.query(conditions[1])[['COUPON_SUCCESS']].mean().values[0]
    
    # Create a DataFrame for comparison
    comparison_df = pd.DataFrame({
        'USER_TYPE': ['Frequent', 'Infrequent'],
        'COUPON_SUCCESS': [success_rate_1, success_rate_2]
    })
    
    # Create a bar chart with Seaborn
    plt.figure(figsize=(10, 6))
    fig = sns.barplot(comparison_df, x='COUPON_SUCCESS', y='USER_TYPE', palette=colors, ci=None)
    
    # Set the title and labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    # Add a note using Matplotlib's text function
    plt.text(0.5, -0.15, note, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
    
    # Add values on the bars
    for p in fig.patches:
        fig.annotate(format(p.get_width(), '.2f'), 
                     (p.get_x() + p.get_width(), p.get_y()), 
                     xytext=(-30, -65), 
                     textcoords='offset points')
    
    # Adjust layout
    plt.tight_layout(pad=3.0)
    plt.subplots_adjust(right=0.9)
    
    # Save plot
    plt.savefig(f'images/plots/{filename}.jpg')
    
    # Show the plot
    plt.show()

# Example usage:
# create_comparison_plot(
#     data=data_only_cheap_restaurant_coupon,
#     conditions=[
#         "(RESTAURANT_LESS_THAN_20 == '4~8') | (RESTAURANT_LESS_THAN_20 == 'gt8')",
#         "not ((RESTAURANT_LESS_THAN_20 == '4~8') | (RESTAURANT_LESS_THAN_20 == 'gt8'))"
#     ],
#     title='Fig5: Acceptance Rate for Cheap Restaurant Goers by Frequency',
#     note='Note: Frequent users visit the restaurant 4 or more times a month.',
#     filename='fig9'
# )