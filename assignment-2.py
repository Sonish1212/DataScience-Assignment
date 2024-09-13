import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
#Loading Dataset file

df1 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset1.csv')
df2 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset2.csv')
df3 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset3.csv')

# Assuming dataset1 and dataset2 are already defined
# and that performance_metrics is a list of the performance-related columns.

performance_metrics = ['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']


# Merge Dataset 1 (which contains gender information) with Dataset 2 (which contains performance metrics)
merged_data_gender = pd.merge(df1[['ID', 'gender']], df2, on='ID')

# Merge Dataset 1 (which contains gender information) with Dataset 2 (which contains performance metrics)
merged_data_deprived = pd.merge(df1[['ID', 'deprived']], df2, on='ID')

# Separate data by gender
male_data = merged_data_gender[merged_data_gender['gender'] == 1]
female_data = merged_data_gender[merged_data_gender['gender'] == 0]


# Seperate data by deprived
deprived_1 = merged_data_deprived[merged_data_deprived['deprived'] == 0]
deprived_2 = merged_data_deprived[merged_data_deprived['deprived'] == 1]


# Perform t-tests for each performance metric
# Perform t-tests for each performance metric by gender
t_test_results_gender = {}
for column in performance_metrics:
    t_stat, p_value = ttest_ind(male_data[column].dropna(), female_data[column].dropna(), equal_var=False)
    t_test_results_gender[column] = {'t-statistic': t_stat, 'p-value': p_value}

# Perform t-tests for each performance metric by deprived status
t_test_results_deprived = {}
for column in performance_metrics:
    t_stat, p_value = ttest_ind(deprived_1[column].dropna(), deprived_2[column].dropna(), equal_var=False)
    t_test_results_deprived[column] = {'t-statistic': t_stat, 'p-value': p_value}

# Convert the t-test results for gender to DataFrame
t_test_results_gender_df = pd.DataFrame(t_test_results_gender).T

# Convert the t-test results for deprived status to DataFrame
t_test_results_deprived_df = pd.DataFrame(t_test_results_deprived).T

# Debug: Check the structure of the DataFrame
print(t_test_results_gender_df.head())  # Check column names and data

# Debug: Check the structure of the DataFrame
print(t_test_results_deprived_df.head())  # Check column names and data


# Define a function for plotting the t-test results
def plot_ttest_results(ax, df, title, xlabel, ylabel, color_stat='skyblue', color_pval='salmon'):
    """
    Plots t-statistics and p-values for the performance metrics on the given axes.
    """
    # Plot t-statistics
    ax[0].barh(df.index, df['t-statistic'], color=color_stat)
    ax[0].set_title(f'T-Statistics for {title}')
    ax[0].set_xlabel(xlabel)
    ax[0].set_ylabel(ylabel)

    # Plot p-values
    ax[1].barh(df.index, df['p-value'], color=color_pval)
    ax[1].set_title(f'P-Values for {title}')
    ax[1].set_xlabel('P-Value')
    ax[1].set_ylabel(ylabel)

# Create subplots for gender and deprived status
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

# Plot gender results
plot_ttest_results(ax[:, 0], t_test_results_gender_df, 
                   title='Performance Metrics by Gender', 
                   xlabel='T-Statistic', ylabel='Performance Metric',
                   color_stat='skyblue', color_pval='salmon')

# Plot deprived status results
plot_ttest_results(ax[:, 1], t_test_results_deprived_df, 
                   title='Performance Metrics by Deprived Status', 
                   xlabel='T-Statistic', ylabel='Performance Metric',
                   color_stat='lightgreen', color_pval='orange')

# Adjust layout for better readability
plt.tight_layout()
plt.show()
