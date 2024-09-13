# 1. Box plots for numerical columns by gender
import pandas as pd
import matplotlib.pyplot as plt

# Loading the CSV files
df1 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset1.csv')
df3 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset2.csv')
df2 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset3.csv')
pd.set_option('display.max_columns', None)

# Merging datasets on 'ID'
merged_df = pd.merge(df1, df2, on='ID', how="inner")
final_df = pd.merge(merged_df, df3, on="ID", how="inner")

# Dropping duplicates
final_df = final_df.drop_duplicates()

# Defining column indices for numerical columns
numerical_column_indices = [4, 5, 6, 7, 8, 9, 10, 11]  # Replace with actual indices for numerical data
numerical_columns = final_df.iloc[:, numerical_column_indices]

categorical_columns = ['gender', 'minority', 'deprived']

# Loop through the categorical columns (minority and deprived) and plot bar plots for each
for cat_column in categorical_columns:
    for column in numerical_columns.columns:
        plt.figure(figsize=(10, 6))
        
        # Calculate the mean for each category in the categorical column (minority or deprived)
        means = final_df.groupby(cat_column)[column].mean()
        
        # Create a bar plot
        means.plot(kind='bar', color=['#ff9999', '#66b3ff'], edgecolor='black')

        plt.title(f'Bar Plot of {column} by {cat_column.capitalize()}')
        plt.xlabel(cat_column.capitalize())
        plt.ylabel(f'Mean of {column}')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()


