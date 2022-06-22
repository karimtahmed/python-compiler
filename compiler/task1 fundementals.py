#!/usr/bin/env python
# coding: utf-8

# In[84]:


y=input("enter equation : ")
equation=list(y)
c=0
z=1
for i in equation :
    if i.isalpha():
        for j in range(len(equation)):
            if equation[c] == equation[j] and c != j:
                print(c,j,equation[c] ,equation[j])
                equation[j]='id'+str(z)
                print(equation)
        
        equation[c]='id'+str(z)
        z=z+1
    c=c+1
equation="".join(equation)
equation    


# In[ ]:




