import pandas as pd
import matplotlib.pyplot as plt

# Loading the CSV files
df1 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset1.csv')
df2 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset2.csv')
df3 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset3.csv')

# Merging datasets on 'ID'
merged_df = pd.merge(df1, df2, on='ID', how="inner")
final_df = pd.merge(merged_df, df3, on="ID", how="inner")

# Dropping duplicates
final_df = final_df.drop_duplicates()

# Defining column indices for ordinal columns
ordinal_columns = final_df.iloc[:, 12:26]  # Adjusting column range for ordinal columns

# Calculating the median for each ordinal column
medians = ordinal_columns.median()

# Plotting histograms with median marked
for column in ordinal_columns:
    plt.figure(figsize=(8, 6))
    plt.hist(ordinal_columns[column], bins=5, edgecolor='black', alpha=0.7)
    plt.axvline(medians[column], color='red', linestyle='dashed', linewidth=1.5, label=f'Median: {medians[column]:.2f}')
    plt.title(f'Distribution of {column} with Median')
    plt.xlabel(f'{column} (Rating)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()
