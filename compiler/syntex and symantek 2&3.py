#!/usr/bin/env python
# coding: utf-8

# In[92]:


y=input("enter equation : ")
equation=list(y)
c=0
z=1
v=0
zl=0
flag=0
l=len(equation)
zeko=0
t=0
eq= ["1", "1", "1", "1"]
for i in range(len(equation)):
    if equation[i].isalpha():
        for j in range(len(equation)):
            if equation[c] == equation[j] and c != j:
                print(c,j,equation[c] ,equation[j])
                equation[j]='id'+str(z)
        equation[c]='id'+str(z)
        z=z+1
        eq[zl]=equation[i]
        zl=zl+1
        print(eq) 
    if i+1 < l :
        flag=0
    else:
        flag=1
    if equation[i].isnumeric():
        if flag==0:
            if equation[i+1] != '*':
                if equation[i+1] == '.':
                    v = equation[i]+equation[i+1]+equation[i+2]
                    zeko=1
                    if i+3 < l:
                        if equation[i+3].isnumeric():
                            v = v + equation[i+3]
                    eq[zl]=v
                    t=zl
                    zl=zl+1
        if equation[i-1] != '.':
            if flag == 1 :
                v = equation[i]
                eq[zl]=v
                t=zl 
                zl=zl+1
                
            else:
                if equation[i+1] != '.':
                    v = equation[i]
                    eq[zl]=v 
                    t=zl
                    zl=zl+1
                    
    c=c+1
equation="".join(equation)
print(eq , equation)
syntex()
semantic()
equation,v
#y=z+2*x


# In[4]:


def syntex():
    print('syntex tree : ')
    print('              id1 ')
    print('                 \ ')
    print('                  = ')
    print('                   \ ')
    print('                    + ')
    print('                   / \ ')
    print('                 '+eq[1]+'  *')
    print('                     / \ ')
    print('                    '+eq[2]+'  '+eq[3])


# In[12]:


syntex()


# In[87]:


def semantic():
    floation=[" "," "," "," "]
    if zeko == 1:
        if t == 1:
            floation[2]='int to float ' + eq[2]
            floation[3]='int to float ' + eq[3]
            floation[1]='                '
        elif t == 2:
            floation[1]='int to float ' + eq[1]
            floation[3]='int to float ' + eq[3]
        elif t == 3:
            floation[1]='int to float ' + eq[1]
            floation[2]='int to float ' + eq[2]
    else:
        floation[t]='int to float '+ eq[t]
        if t != 1:
            floation[1]='                '
    print('semantic tree : ')
    print('              id1 ')
    print('                 \ ')
    print('                  = ')
    print('                   \ ')
    print('                    + ')
    print('                   / \ ')
    print('                 '+eq[1]+'  *')
    print('    '+floation[1]+' / \ ')
    print('                    /   \ ')
    print('                   '+eq[2]+'   '+eq[3])
    print('        '+floation[2]+'          '+floation[3])


# In[88]:


semantic()


# In[ ]:




