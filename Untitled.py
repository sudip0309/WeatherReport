#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
sns.set(color_codes=True)


# In[2]:


weather = pd.read_csv(r"C:\Users\Sudip\Downloads\weatherHistory.csv")


# In[3]:


weather.head()


# In[4]:


weather.info()


# In[5]:


sns.barplot(weather['Temperature (C)'], weather['Humidity'])


# In[6]:


sns.distplot(weather['Humidity'])


# In[7]:


sns.jointplot(weather['Temperature (C)'], weather['Humidity'])


# In[8]:


sns.jointplot(weather['Temperature (C)'], weather['Humidity'], kind="hex")


# In[9]:


sns.jointplot(weather['Temperature (C)'], weather['Humidity'], kind="kde")


# In[10]:


sns.pairplot(weather[['Temperature (C)','Humidity', 'Wind Speed (km/h)']])


# In[11]:


sns.stripplot(weather['Summary'], weather['Humidity'])


# In[12]:


sns.stripplot(weather['Summary'], weather['Humidity'], jitter=True)


# In[ ]:


sns.swarmplot(weather['Temperature (C)'], weather['Humidity'])


# In[ ]:


sns.boxplot(weather['Temperature (C)'], weather['Humidity'], hue=weather['Daily Summary'])


# In[ ]:


sns.barplot(weather['Temperature (C)'], weather['Humidity'], hue=weather['Daily Summary'])


# In[ ]:


sns.countplot(weather['Daily Summary'])


# In[ ]:


sns.pointplot(weather['Temperature (C)'], weather['Humidity'], hue=weather['Daily Summary'])


# In[ ]:


sns.lmplot(x='Temperature (C)', y='Humidity', data=weather)


# In[ ]:


sns.lmplot(x='Temperature (C)', y='Humidity', hue='Daily Summary', data=weather)


# In[ ]:




