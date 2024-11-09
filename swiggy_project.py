                              #Project Title - Analyzing Swiggy ( Bangalore Outlet )




#Load 'numpy' and 'pandas' for manipulating numbers and data frames
#Load 'matplotlib.pyplot' and 'seaborn' for data visualisation
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Swiggy dataset
swiggy_data = pd.read_csv('C:\\Users\\ANISH\\Downloads\\Swiggy data.csv')
print(swiggy_data.head())
print(swiggy_data.shape)                                                          #get the dimention of the dataframe
print(swiggy_data.index)                                                            #get the row no. of datframe
print(swiggy_data.columns)                                                          #get colums of dataframe
print(swiggy_data.info())                                                           #Look at the basic information about the dataframe


# Exploratory Data Analysis (EDA)

#Check for missing values
print(data.isnull().sum())

# Basic Statistics
print(swiggy_data.describe())

# Visualize Distribution of Cost for Two so create the histogram chart
plt.figure(figsize=(11,6))
sns.histplot(data=swiggy_data, x='Cost_for_Two', color='green', edgecolor='black', alpha=0.5, bins=30)
plt.title('Distribution of Cost for Two',fontsize=20)
plt.xlabel('Cost for Two')
plt.ylabel('Count')
plt.xticks(rotation=45,ha='right')
plt.show()


#Count of Shops by Cuisine Type so Create the Count plot
plt.figure(figsize=(14,6))
sns.countplot(data=swiggy_data, y='Cuisine',edgecolor='black',order=swiggy_data['Cuisine'].value_counts().index[:20])
plt.title('Count of Shops by Cuisine Type(Top 20)',fontsize=20)
plt.xlabel('Count')
plt.ylabel('Cuisine Types')
plt.show()


# Average Rating by Location
plt.figure(figsize=(12, 6))
sns.barplot(data=swiggy_data,x='Location', y='Rating',color='orange',edgecolor='black',order=swiggy_data['Location'].value_counts().index[:20])
plt.title('Average Rating by Location(Top 20)',fontsize=20)
plt.xlabel('Location')
plt.ylabel('Average Rating')
plt.xticks(rotation=45,ha='right')                                  #Rotate lable foe better readability
plt.show()


# Correlation Matrix Heatmap
plt.figure(figsize=(11, 6))
sns.scatterplot(data=swiggy_data,x='Rating',y='Cost_for_Two',color='blue',edgecolor='black',alpha=0.9)
plt.title('Scatter Plot for Rating and Cost for Two', fontsize=20)
plt.xlabel('Rating')
plt.ylabel('Cost for Two')
plt.grid(color='k',linestyle='--',linewidth=0.2)
plt.show()

