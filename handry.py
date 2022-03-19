#!/usr/bin/env python
# coding: utf-8

# In[5]:


x = 6
y = 0
try:
print(x/y)
except:
print("Error : division by Zero is not allowed")


# In[12]:


x = 6
y = 0
try:
    k = x/y  # raises divide by zero exception.
    print(k)
except ZeroDivisionError:
    print("You Can Not divide by zero buddy!!")
finally:
    # this block is always executed
    # regardless of exception generation.
    print('Dividing by zero is not allowed!!')


# In[27]:


# Consider a dataset that has y and y as points
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 8, 3,])
y = np.array([3, 10, 5,])

plt.plot(xpoints, ypoints, 'o')
plt.show()


# In[18]:



import matplotlib.pyplot as plt
import numpy as np
# Create a Figure with 2 rows and 2 columns of subplots:
fig, ax = plt.subplots(2, 2)

x = np.linspace(0, 5, 100)

# Index 4 Axes arrays in 4 subplots within 1 Figure: 
ax[0, 0].plot(x, np.sin(x), 'g') #row=0, column=0
ax[1, 0].plot(range(100), 'b') #row=1, column=0
ax[0, 1].plot(x, np.cos(x), 'r') #row=0, column=1
ax[1, 1].plot(x, np.tan(x), 'k') #row=1, column=1

plt.show()


# In[ ]:




