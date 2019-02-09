
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
from pandas import datetime
import numpy as np
from datetime import datetime as dt
get_ipython().magic('matplotlib inline')


# In[2]:

#import data
year_data = pd.read_csv('G:\\year_wise_data.csv',index_col=0)
print(year_data.head())

qtr_arr_data = pd.read_excel('G:\\qtr_wise_data.xlsx',index_col=0)
print(qtr_arr_data.head())

#Combined fta data is the original data set we will be using 
combined_fta_data = pd.read_excel('G:\\fta_data.xlsx',index_col=0)
print(combined_fta_data.head())

#Fta month wise data 
fta_month_wise_data = pd.read_excel('G:\\year_wise_fta.xlsx',index_col=0)
print(fta_month_wise_data.head())


# In[3]:

#trend plot of FTA
#Create background
fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(15,4))
#Plot Trend Plot
combined_fta_data['FTAs'].plot(ax=axes,title="Trend Plot",colormap='hsv', 
legend=False)


# In[4]:

#Create a month name column in the dataframe
combined_fta_data['Month_name'] = combined_fta_data.index.month
#Create group based on month number 1,2,3 ...
x = combined_fta_data['FTAs'].groupby(combined_fta_data['Month_name']).mean()
#Reindex the series on month name Jan, Feb ...
x.reindex(index=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
#Indexing it again to resolve error
x.index = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#Create background
fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(10,5))
#Plot horizontal bar graph
x.plot(kind='bar',ax=axes,colormap='PuOr',legend=False)


# In[5]:

#Read the data
fta_data =pd.read_excel('G:\\year_wise_ftay.xlsx',index_col=0)
fta_data.head()
fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(10,5))
fta_data.boxplot()


# In[7]:

#Plot FTA and Rainfall
fig,axes=plt.subplots(figsize=(14,6),nrows=2,ncols=1)
axes[0].plot(combined_fta_data.index,combined_fta_data[['FTAs']],'b-')
axes[1].plot(combined_fta_data.index,combined_fta_data[['Rainfall']])
plt.tight_layout()
fig.show()


# In[8]:

#Create a Month name column in the dataframe
combined_fta_data['Month'] = combined_fta_data.index.month

#Create group based on month number 1,2,3 ...
y = combined_fta_data['Rainfall'].groupby(combined_fta_data['Month']).mean()

#Reindex the series on Month name Jan, feb ...
y.reindex(index=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])
y.index = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

#Create background
fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(10,5))

#Plot horizontal histogram
y.plot(kind='bar',title="Month-wise plot of Rainfall data",ax=axes,colormap='spring',legend=False)


# In[9]:

#Create a Quarter name column in the dataframe
combined_fta_data['Quarter'] = combined_fta_data.index.quarter
#Create group based on quarter number 1,2,3 ...
y = combined_fta_data['Rainfall'].groupby(combined_fta_data['Quarter']).mean()
#Reindex the series on quarter name Qtr1, Qtr2 ...
y.reindex(index=['Qtr1','Qtr2','Qtr3','Qtr4'])
y.index=['Qtr1','Qtr2','Qtr3','Qtr4']
#Create background
fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(10,5))
#Plot horizontal histogram
y.plot(kind='bar',ax=axes,colormap='autumn',legend=False)


# In[10]:

rainfall_data = pd.read_excel('G:\\fta_datay.xlsx',index_col=0)
rainfall_data.head()
fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(10,5))
rainfall_data.boxplot()


# In[12]:

#Plot FTA and Temperature
#temp_data = pd.read_excel('E:/ProgAnalytics/Project/fta_data.xlsx',index_col=0)
fig,axes=plt.subplots(figsize=(14,6),nrows=2,ncols=1)
axes[0].plot(combined_fta_data.index,combined_fta_data[['FTAs']],'b-')
axes[1].plot(combined_fta_data.index,combined_fta_data[['Temperature']])
plt.tight_layout()
fig.show()


# In[13]:

# Monthly Temperature Plots
#Create a month name column in the dataframe
combined_fta_data['Month_name'] = combined_fta_data.index.month
#Create group based on month number 1,2,3 ...
x=combined_fta_data['Temperature'].groupby(combined_fta_data['Month_name']).mean()
#Reindex the series on month name Jan, Feb ...
x.reindex(index=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
#Indexing it again to resolve error
x.index = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

#Create background
fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(10,5))
#Plot vertical bar graph
x.plot(kind='bar',ax=axes,colormap='Paired',legend=True,title="Monthly Temperature Plot")


# In[14]:

#Create a Quarter name column in the dataframe
combined_fta_data['Quarterr'] = combined_fta_data.index.quarter

#Create group based on quarter number 1,2,3 ...
y = combined_fta_data['Temperature'].groupby(combined_fta_data['Quarterr']).mean()

#Reindex the series on quarter name Qtr1, Qtr2 ...
y.reindex(index=['Qtr1','Qtr2','Qtr3','Qtr4'])
y.index=['Qtr1','Qtr2','Qtr3','Qtr4']

#Create background
fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(10,5))

#Plot horizontal histogram
y.plot(kind='bar',ax=axes,title="Quarter-wise Temp. data",colormap='bwr',legend=False)


# In[24]:

fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(14,5))
year_temp = pd.read_excel('G:\\year_temp.xlsx',index_col=0)
year_temp.boxplot()


# In[15]:

#Plot of rolling correlation between FTAs and Rainfall
fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(14,7))
corr = pd.rolling_corr(combined_fta_data['FTAs'],combined_fta_data['Rainfall'],12)
corr.plot(style='k-',ax=axes)


# In[16]:

fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(14,7))
corr = pd.rolling_corr(combined_fta_data['Rainfall'],combined_fta_data['Temperature'],12)
corr.plot(style='k-',ax=axes,legend=True,label="Moving correlation")


# In[17]:

#Plot of rolling correlation between FTAs and Temperature
fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(14,7))
corr1 = combined_fta_data['FTAs'].rolling(12).corr(combined_fta_data['Temperature'])
corr1.plot(style='k-',ax=axes,title="Correlation Between FTA and Temperature",legend=False)


# In[25]:

import seaborn as sns
fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(10,5))
kd = combined_fta_data['FTAs'].plot.kde()
kd.set_xlabel("Number of FTAs")
kd.set_ylabel("Density")
kd.plot(label="Density Plot of Foreign Tourist Arrival",legend=False,shade=True, color='r')


# In[27]:

fig,axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True,figsize=(10,5))
kd = combined_fta_data['Rainfall'].plot.kde()
kd.set_xlabel("Number of FTAs")
kd.set_ylabel("Density")
kd.plot(label="Density Plot of Rainfall",legend=False,shade=True, color='r')

