#importing necessary dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import scipy.stats
from scipy.stats import kurtosis

#Reading the csv files
df1 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset1.csv')
df2 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset2.csv')
df3 = pd.read_csv('C:/Users/singh/OneDrive/Desktop/data science code/dataset3.csv')


#dataset1.head()
#dataset2.head()
#dataset3.head()

df = df1.merge(df2, on = "ID", how = "left")
df = df.merge(df3, on="ID", how = 'left')

cleandf = df.dropna()
cleandf.isna().sum()

cleandf.head()

#Descriptive Analysis
cleandf['gender'].value_counts().plot.bar()
plt.show()

cleandf['minority'].value_counts().plot(kind='pie', labels = ["Majority","Others"])
plt.title('Class Distribution')
plt.show()


#Regression
mean_digital_daily_screen_time= cleandf[['C_we','C_wk','G_we','G_wk','S_we','S_wk','T_we','T_wk']].mean(axis = 1)
#print(mean_digital_daily_screen_time)

mean_well_being = cleandf[['Optm','Usef','Relx','Intp','Engs','Dealpr','Thcklr','Goodme','Clsep','Conf','Mkmind','Loved','Intthg','Cheer']].mean(axis = 1)
#print(mean_well_being)

#Inferential Analysis
kurtosis_mean_well_being = kurtosis(mean_well_being)
print(kurtosis_mean_well_being)

kurtosis_mean_digital_daily_screen_time = kurtosis(mean_digital_daily_screen_time)
print(kurtosis_mean_digital_daily_screen_time)

cleandf['mean_well_being'] = mean_well_being
cleandf['mean_digital_daily_screen_time'] = mean_digital_daily_screen_time

model = LinearRegression()

#print(cleaned_dataset[['mean_digital_daily_screen_time','mean_well_being']])

y= cleandf.iloc[:,-2]
x= cleandf.iloc[:,-1]

#Regression
x = sm.add_constant(x)

result = sm.OLS(y,x).fit()
# Print out the results

print(result.summary())
