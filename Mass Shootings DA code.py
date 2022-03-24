#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# In[3]:


df18 = pd.read_csv(r'C:\Users\acer\Documents\US Mass Shootings\shootings_2018.csv')
df19 = pd.read_csv(r'C:\Users\acer\Documents\US Mass Shootings\shootings_2019.csv')
df20 = pd.read_csv(r'C:\Users\acer\Documents\US Mass Shootings\shootings_2020.csv')
df21 = pd.read_csv(r'C:\Users\acer\Documents\US Mass Shootings\shootings_2021.csv')
df22 = pd.read_csv(r'C:\Users\acer\Documents\US Mass Shootings\shootings_2022.csv')
mass_shootings = pd.concat([df18, df19, df20, df21, df22])


# In[4]:


mass_shootings.head()


# In[5]:


df_count = mass_shootings.groupby(['State']).size().reset_index(name='Incidents')

df_count.head()


# In[6]:


code = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN',
    'MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','OH','OK','OR','PA','PR','RI','SC','SD','TN','TX','VI','UT','VA','WA',
    'WA','WA','WV','WI','WY']
df = df_count.assign(Codes=code)
df.head()


# In[7]:


fig = px.choropleth(df, 
                    locations="Codes",  # DataFrame column with locations
                    color="Incidents",  # DataFrame column with color values
                    hover_name="State", # DataFrame column hover info
                    locationmode = 'USA-states') # Set to plot as US States
fig.update_layout(title_text = 'Mass Shoting Incidents since 2018 by State', geo_scope='usa',)

fig.show() 


# In[8]:


df_bar = mass_shootings.groupby(['State']).sum()[["Dead", "Injured", "Total"]].sort_values("Total")
df_bar = df_bar.drop(columns=['Total'])

df_bar.head()


# In[9]:


title_text = "Mass Shooting Victims by State since 2018" 
ax = df_bar.plot.barh(stacked=True, figsize=(14, 12), title = title_text).grid(axis='x')
plt.legend(loc='lower right', fontsize=20)
plt.show()


# In[ ]:




