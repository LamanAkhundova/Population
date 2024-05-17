import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_dataset(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = 'Outflows of foreign population by nationality.xls'
df = load_dataset(file_path)
if df is not None:
    missing_values = df.isnull().sum()
    print("Missing values in the dataset:")
    print(missing_values)
else:
    print("Dataset could not be loaded.")
def check_unique_values(df, column_name):
    unique_values = df[column_name].unique()
    print(f"Unique values in the '{column_name}' column:")
    print(unique_values)
    return unique_values

if df is not None:
    unique_genders = check_unique_values(df, 'Gender')
    unique_ad_clicks = check_unique_values(df, 'AD clicks')
def verify_consistency(unique_values, expected_values, column_name):
    consistent = set(expected_values).issubset(unique_values)
    print(f"The '{column_name}' column has consistent entries." if consistent else f"The '{column_name}' column does not have consistent entries.")
    return consistent

if df is not None:
    gender_consistent = verify_consistency(unique_genders, ['M', 'F'], 'Gender')
    clicks_consistent = verify_consistency(unique_ad_clicks, ['Clicked', 'Not Used', 'Used'], 'AD clicks')
if df is not None:
    print("Column names in the DataFrame:")
    print(df.columns)
def analyze_click_trends(df):
    pivot_table = df.pivot_table(index='Gender', columns='AD clicks', aggfunc='size', fill_value=0)
    print("Pivot table for click trends by gender:")
    print(pivot_table)
    
    total_users_by_gender = pivot_table.sum(axis=1)
    pivot_table['Click Rate'] = pivot_table['Clicked'] / total_users_by_gender

    print("Click rates by gender:")
    print(pivot_table['Click Rate'])

    return pivot_table

if df is not None:
    pivot_table = analyze_click_trends(df)
def plot_click_trends(pivot_table):
    ax = pivot_table[['Clicked', 'Not Used', 'Used']].plot(kind='bar', color=['red', 'blue', 'green'], alpha=0.5)
    plt.title('Clicks by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Number of Clicks')
    plt.xticks(rotation=0)
    plt.legend(['Clicked', 'Not Used', 'Used'], loc='upper right')

    # Displaying values on bars
    for container in ax.containers:
        ax.bar_label(container, fmt='%d')

    plt.show()

file_path = 'Outflows of foreign population by nationality.xls'
df = load_dataset(file_path)

if df is not None:
    # Check for expected columns
    expected_columns = ['Gender', 'AD clicks']
    if not all(column in df.columns for column in expected_columns):
        print(f"Error: Dataset does not contain the expected columns: {expected_columns}")
    else:
        check_missing_values(df)
        
        unique_genders = check_unique_values(df, 'Gender')
        unique_ad_clicks = check_unique_values(df, 'AD clicks')
        
        verify_consistency(unique_genders, ['M', 'F'], 'Gender')
        verify_consistency(unique_ad_clicks, ['Clicked', 'Not Used', 'Used'], 'AD clicks')
        
        pivot_table = analyze_click_trends(df)
        plot_click_trends(pivot_table)
else:
    print("Failed to load dataset.")
