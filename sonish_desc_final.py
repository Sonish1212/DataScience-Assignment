import pandas as pd
import matplotlib.pyplot as plt

# Loading the CSV files
df1 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset1.csv')
df3 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset2.csv')
df2 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset3.csv')
pd.set_option('display.max_columns', None)

# Merging datasets on 'ID'
merged_df = pd.merge(df1, df2, on='ID', how='inner')  # Merge df1 and df2 on 'ID'
print(merged_df.columns)

final_df = pd.merge(merged_df, df3, on='ID', how='inner')  # Merge the result with df3 on 'ID'

# Checking the structure of the final merged DataFrame


# Dropping duplicates
final_df = final_df.drop_duplicates()

# Defining column indices for numerical columns
# numerical_column_indices = [4, 5, 6, 7, 8, 9, 10, 11]  # Replace with actual indices for numerical data
numerical_columns = merged_df.iloc[:, 4:12]
print(numerical_columns)
# Categorical columns for grouping
# categorical_columns = ['gender', 'minority', 'deprived']

# # Loop through each categorical variable and generate a figure for each
# for cat_column in categorical_columns:
#     plt.figure(figsize=(14, 10))
    
#     # Number of subplots based on the number of numerical columns
#     num_plots = len(numerical_columns.columns)
    
#     # Create subplots for each numerical column
#     for i, column in enumerate(numerical_columns.columns, 1):
#         plt.subplot(2, (num_plots // 2) + (num_plots % 2), i)
        
#         # Calculate the mean for each category in the categorical column
#         means = final_df.groupby(cat_column)[column].mean()
        
#         # Create a bar plot for the current column
#         means.plot(kind='bar', color=['#ff9999', '#66b3ff'], edgecolor='black')
        
#         plt.title(f'{column}')
#         plt.xlabel(cat_column.capitalize())
#         plt.ylabel('Mean')
#         plt.tight_layout()

#     # Set the main title for the figure
#     plt.suptitle(f'Bar Plots of Numerical Columns by {cat_column.capitalize()}', fontsize=16)
    
#     # Show the complete figure
#     plt.show()
