#!/usr/bin/env python
# coding: utf-8

# # Importing the Data:
# ## Importing the Fifa 23 career mode data: 

# In[1]:


import pandas as pd


# In[2]:


fifa = pd.read_csv('Fifa 23 Players Data.csv')


# In[3]:


print(fifa)


# In[4]:


print(fifa.head(3))


# # Reading Data in Pandas

# In[5]:


#Read the Headers:
fifa.columns


# In[6]:


#Read a specific column
print(fifa['Known As'])


# In[7]:


#first five 
print(fifa['Known As'][0:5])


# In[8]:


#Multiple Columns - double bracket as it's a list. 
print(fifa[['Known As', 'Overall']][0:5])


# In[9]:


print(fifa.iloc[1])


# In[10]:


#We want to get the 7th row and first column
print(fifa.iloc[7,1])


# In[11]:


#Iterate through rows 
for index, row in fifa.iterrows():
    print(index, row)


# In[12]:


#Getting rows based on a specific condition
fifa.loc[fifa['Best Position'] == 'ST']


# In[13]:


#High Level description
fifa.describe()


# In[14]:


#describe certain columns
fifa[['CDM Rating', 'RWB Rating']].describe()


# In[15]:


#Sorting alphabetically
fifa.sort_values('Full Name')


# In[16]:


#other way 
fifa.sort_values('Full Name', ascending=False)


# In[17]:


#sorting on multiple columns
#1 = ascending, 0 = decending 
fifa.sort_values(['Overall','Potential'], ascending=[0,0])


# In[18]:


#Adding a new column - the BMI of each player. 
fifa['BMI'] = fifa['Weight(in kg)']/(fifa['Height(in cm)']/100)**2


# In[19]:


print(fifa.head(5))


# In[20]:


#Which positions on average have the highest wage in euros?
wages = fifa.groupby('Best Position').mean()['Wage(in Euro)']
print(wages)


# In[21]:


#Visualise this
import matplotlib.pyplot as plt

wages.plot.bar()
plt.ylabel("Average Weekly Wage")
plt.title("Average Weekly Wage in Euros by position")


# In[22]:


#How many players are right and left footed?
foot = fifa.groupby('Preferred Foot').count()[['Known As']]


# In[23]:


foot.plot.pie(subplots=True)


# In[24]:


#which nations are most popular?
nationality_split = fifa['Nationality'].value_counts().reset_index(name='Count of Nationality')


# In[25]:


#treemap of this data
nationality_split.rename(columns={'index':'Nationality'})


# In[26]:


import squarify


# In[27]:


squarify.plot(sizes=nationality_split['Count of Nationality'], label=nationality_split['index'], alpha=.8)
plt.axis('off')
plt.show()


# In[28]:


#Alternatively we can turn a value_counts to a data frame by using: .value_counts().to_frame()


# In[29]:


#this graph is very cluttered so i'll only look at the biggest ten nations
top_10 = nationality_split[0:11]


# In[30]:


squarify.plot(sizes=top_10['Count of Nationality'], label=top_10['index'], alpha=.8)


# In[31]:


#Is there a link between BMI and the overall of football players? This analysis will only be for 25 and under
under_25 = fifa.loc[fifa['Age']<=25]


# In[32]:


under_25


# In[33]:


plt.scatter(under_25['BMI'], under_25['Overall'], label='Data Points', alpha=0.6, color='blue', s=75)
plt.xlabel('BMI')
plt.ylabel('Overall Rating')


# In[40]:


#This just looks like a blob, let us take the top 200 under 25 players. 
top_200_u25 = under_25 = fifa.loc[fifa['Age']<=25][:200]

print(top_200_u25)


# In[37]:





# In[38]:


#Linear Regression 
from sklearn import linear_model


# In[45]:


reg = linear_model.LinearRegression()
reg.fit(top_200_u25[['BMI']],top_200_u25['Overall'])


# In[47]:


reg.coef_


# In[49]:


reg.intercept_


# In[58]:


#What's the correlation between potential and value for under 25 players? 
plt.scatter(top_200_u25['Potential'], top_200_u25['Value(in Euro)'], label='Data Points', alpha=0.6, color='blue', s=75)
plt.xlabel('Potential')
plt.ylabel('Value (in Euro)(bn)')


# In[55]:


reg2 = linear_model.LinearRegression()
reg2.fit(top_200_u25[['Potential']],top_200_u25['Value(in Euro)'])


# In[57]:


reg.predict([[89]])


# In[59]:


coef = reg.coef_


# In[60]:


inte = reg.intercept_


# In[61]:


# y = mx + b 
coef*89 + inte


# In[64]:


plt.scatter(top_200_u25['Potential'], top_200_u25['Value(in Euro)'])
plt.plot(top_200_u25['Potential'], reg2.predict(top_200_u25[['Potential']]))
plt.xlabel('Potential')
plt.ylabel('Value (in Euro)(bn)')


# In[ ]:




