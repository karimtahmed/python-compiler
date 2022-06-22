#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[4]:


re1="(\\+|-)\\d+"
re2="[A-Za-z][A-Za-z|\\d|\\_]"
re3="[E|e]nd$|[E|e]lse$|[U|u]ntil$"
re4="\\>|\\<|\\≤"
re5="%%[\\sA-Za-z\\d\\>|\\<|\\≤]*"
x1=input('Please enter an example of Numbers: ')
L1 = re.search(re1, x1)
if L1:
  print("True")
else:
  print("False")
x1=input('Please enter an example of Identifiers:  ')
L2 = re.search(re2, x1)
if L2:
  print("True")
else:
  print("False")
x1=input('Please enter an example of Reserved Words: ')
L3 = re.search(re3, x1)
if L3:
  print("True")
else:
  print("False")
x1=input('Please enter an example of Special symbols:  ')
L4 = re.search(re4, x1)
if L4:
  print("True")
else:
  print("False")
x1=input('Please enter an example of Comment:')
L5 = re.search(re5, x1)
if L5:
  print("True")
else:
  print("False")


# In[ ]:





# In[ ]:




