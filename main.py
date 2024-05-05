import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your dataset into a DataFrame
df = pd.read_excel('Outflows of foreign population by nationality.xls')


# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in the dataset:")
print(missing_values)

# Unique values in 'Gender' and 'AD clicks' columns
unique_genders = df['Gender'].unique()
unique_ad_clicks = df['AD clicks'].unique()

print("Unique values in the 'Gender' column:")
print(unique_genders)
print("Unique values in the 'AD clicks' column:")
print(unique_ad_clicks)

# Verify consistency in Gender Column
gender_consistent = set(['M', 'F']).issubset(unique_genders)
print("The 'Gender' column has consistent entries." if gender_consistent else "The 'Gender' column does not have consistent entries.")

# Verify consistency in AD clicks Column
clicks_consistent = set(['Clicked', 'Not Used', 'Used']).issubset(unique_ad_clicks)
print("The 'AD clicks' column has consistent entries." if clicks_consistent else "The 'AD clicks' column does not have consistent entries.")

# Print column names
print("Column names in the DataFrame:")
print(df.columns)

# Analyze click trends by gender using pivot table
pivot_table = df.pivot_table(index='Gender', columns='AD clicks', aggfunc='size', fill_value=0)

print("Pivot table for click trends by gender:")
print(pivot_table)

# Calculate click rates
total_users_by_gender = pivot_table.sum(axis=1)
pivot_table['Click Rate'] = pivot_table['Clicked'] / total_users_by_gender

print("Click rates by gender:")
print(pivot_table['Click Rate'])

# Plotting
pivot_table.plot(kind='bar', color=['red', 'blue', 'green'], alpha=0.5)
plt.title('Clicks by Gender')
plt.xlabel('Gender')
plt.ylabel('Click')
plt.xticks(rotation=0)
plt.legend(['Clicked', 'Not Used', 'Used'], loc='upper right')

# Displaying values on bars
for container in plt.gca().containers:
    plt.gca().bar_label(container, fmt='%d')

plt.show()

