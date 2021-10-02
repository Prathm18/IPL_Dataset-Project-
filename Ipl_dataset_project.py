#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[5]:


import os
os.chdir('/storage/emulated/0/tempPic')


# In[6]:


import pandas as pd
#read the matches.csv data file from directory
ipl = pd.read_csv("matches.csv")


# In[9]:


#Looking at 1st five records of ipl data 
ipl.head()


# In[10]:


#checking of how many row ans column
ipl.shape


# In[12]:


#getting the frequency of most man of the match by  player
ipl["player_of_match"].value_counts()


# In[13]:


#getting top 10 player who win man of the match award
ipl["player_of_match"].value_counts()[0:10]


# In[16]:


#getting the names of player who wins the man of the match award 
list(ipl["player_of_match"].value_counts()[0:5].keys())


# In[29]:


#plotting the bar plot of player of match
plt.figure(figsize=(8,5))
plt.xlabel("Man Of The Match Player")
plt.ylabel("Counts")
plt.bar(list(ipl["player_of_match"].value_counts()[0:5].keys()),list(ipl["player_of_match"].value_counts()[0:5]),color="g")
plt.show()


# In[31]:


ipl["result"].value_counts()


# In[32]:


ipl["toss_winner"].value_counts()


# In[51]:


batting_first=ipl[ipl["win_by_runs"]!=0]
batting_first.head()


# In[52]:


plt.figure(figsize=(4,4))
plt.hist(batting_first["win_by_runs"],bins=30)
plt.title("Distribution of runs")
plt.xlabel("Runs")
plt.show()


# In[35]:


batting_first["winner"].value_counts()


# In[45]:


plt.figure(figsize=(6,6))
plt.bar(list(batting_first["winner"].value_counts()[0:3].keys()),list(batting_first["winner"].value_counts()[0:3]),color=["blue","yellow","orange"])
plt.show()


# In[52]:


plt.figure(figsize=(5,5))
plt.pie(list(batting_first["winner"].value_counts()),labels=list(batting_first["winner"].value_counts().keys()),autopct="%0.1f%%")
plt.show()


# In[8]:


second_batting=ipl[ipl["win_by_wickets"]!=0]
second_batting.head()


# In[9]:


plt.figure(figsize=(4,4))
plt.hist(second_batting["win_by_wickets"],bins=20)
plt.title("Distribution of wickets")
plt.xlabel("wickets")
plt.show()


# In[58]:


second_batting["winner"].value_counts()


# In[59]:


plt.figure(figsize=(6,6))
plt.bar(list(second_batting["winner"].value_counts()[0:3].keys()),list(second_batting["winner"].value_counts()[0:3]),color=["purple","blue","yellow"])
plt.show()


# In[63]:


plt.figure(figsize=(5,5))
plt.pie(list(second_batting["winner"].value_counts()),labels=list(second_batting["winner"].value_counts().keys()),autopct="%0.1f%%")
plt.show()


# In[10]:


ipl["season"].value_counts()


# In[11]:


ipl["city"].value_counts()


# In[13]:


import numpy as np
np.sum(ipl["toss_winner"]==ipl["winner"])


# In[15]:


393/635


# In[20]:


import os
os.chdir('/storage/emulated/0/tempPic')


# In[21]:


import pandas as pd
deliveries = pd.read_csv("deliveries.csv")


# In[23]:


deliveries.head()


# In[25]:


deliveries["match_id"].unique()


# In[30]:


match1=deliveries[deliveries["match_id"]==1]


# In[31]:


match1.head()


# In[34]:


match1.shape


# In[36]:


srh=match1[match1["inning"]==1]


# In[39]:


srh["batsman_runs"].value_counts()


# In[41]:


srh["dismissal_kind"].value_counts()


# In[46]:


rcb=match1[match1["inning"]==2]


# In[47]:


rcb["batsman_runs"].value_counts()


# In[49]:


rcb["dismissal_kind"].value_counts()

