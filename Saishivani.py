#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
df=pd.read_csv('C:/Users/DELL/Desktop/Sample - Superstore.csv')
print(df)


# In[12]:


#monthlysales
import pandas as pd
df=pd.read_csv('C:/Users/DELL/Desktop/Sample - Superstore.csv')
ms=df.groupby(df.OrderDate)['Sales'].sum()
print(ms)


# In[18]:


#Salesbycategory
import pandas as pd
df=pd.read_csv('C:/Users/DELL/Desktop/Sample - Superstore.csv')
sc=df.groupby('Category')['Sales'].sum().reset_index()
print(sc)


# In[17]:


#monthlyprofits
import pandas as pd
df=pd.read_csv('C:/Users/DELL/Desktop/Sample - Superstore.csv')
Mp=df.groupby(df.OrderDate)['Profit'].sum().reset_index()
print(Mp)


# In[20]:


#profit analysis by category
import pandas as pd
df=pd.read_csv('C:/Users/DELL/Desktop/Sample - Superstore.csv')
pc=df.groupby('Category')['Profit'].sum().reset_index()
print(pc)


# In[21]:


import pandas as pd
df=pd.read_csv('C:/Users/DELL/Desktop/Sample - Superstore.csv')
print(df)


# In[22]:


import pandas as pd
df=pd.read_csv('C:/Users/DELL/Desktop/Sample - Superstore.csv')
df.head()


# In[ ]:




