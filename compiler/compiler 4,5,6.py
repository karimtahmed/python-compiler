#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
        isf=int(eq[t])
        pri=eq[t] #to print int number while also print in tree float
        isf = float(isf)
        eq[t]=str(isf)
        floation[t]='int to float '+ pri
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
    print('    '+floation[1]+'  / \ ')
    print('                     /   \ ')
    print('                   '+eq[2]+'   '+eq[3])
    print('        '+floation[2]+'          '+floation[3])


# In[52]:


y=input("enter equation : ")
equation=list(y)
c=0
z=1
v=0
zl=0
flag=0
l=len(equation)
again=0
zeko=0 #flag if = 1 then number is float
t=0 #value of number
eq= ["1", "1", "1", "1"]
for i in range(len(equation)):
    if equation[i].isalpha():
        for j in range(len(equation)):
            if equation[c] == equation[j] and c != j:
                print(c,j,equation[c] ,equation[j])
                equation[j]='id'+str(z)
                again=1
                s=z
        equation[c]='id'+str(z)
        eq[zl]=equation[i]
        z=z+1
        zl=zl+1
        print(eq)
    if again == 1 :
            if t == 1:
                eq[2]='id'+str(s)
                eq[3]='id'+str(s)
            elif t == 2:
                eq[1]='id'+str(s)
                eq[3]='id'+str(s)
            elif t == 3:
                eq[1]='id'+str(s)
                eq[2]='id'+str(s)
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
ICG()
code_optimizer()
code_generator()
equation,v
#y=z+2*x


# In[39]:


def ICG():
    print('ICG : ')
    if t == 3:
        if zeko == 0:
            print("    t1 = int to float", v)
            print("    t2 = t1 *",eq[2])
            print("    t3 = t2 +",eq[1])
            print("    id1 = t3")
        elif zeko == 1:
            if eq[2] != eq[1]:
                print("    t1 = int to float id2")
                print("    t2 = int to float id3")
                print("    t3 = t2 *",v)
                print("    t4 = t3 + t1 ")
                print("    id1 = t4")
            else:
                print("    t1 = int to float id2")
                print("    t2 = t1 *",v)
                print("    t3 = t2 + t1 ")
                print("    id1 = t3")
    elif t == 2:
        if zeko == 0:
            print("    t1 = int to float", v)
            print("    t2 = t1 *",eq[3])
            print("    t3 = t2 +",eq[1])
            print("    id1 = t3")
        elif zeko == 1:
            if eq[2] != eq[1]:
                print("    t1 = int to float id2")
                print("    t2 = int to float id3")
                print("    t3 = t2 *",v)
                print("    t4 = t3 + t1 ")
                print("    id1 = t4")
            else:
                print("    t1 = int to float id2")
                print("    t2 = t1 *",v)
                print("    t3 = t2 + t1 ")
                print("    id1 = t3")
    elif t == 1 :
        if zeko == 0:
            if eq[2] != eq[1]:
                print("    t1 = int to float", v)
                print("    t2 = id2 * id3 ")
                print("    t3 = t1 + t2 ")
                print("    id1 = t3")
            else:
                print("    t1 = int to float", v)
                print("    t2 = id2 * id2 ")
                print("    t3 = t1 + t2 ")
                print("    id1 = t3")
        elif zeko == 1:
            if eq[2] != eq[1]:
                print("    t1 = int to float id2")
                print("    t2 = int to float id3")
                print("    t3 = t1 * t2")
                print("    t4 = t3 +",v)
                print("    id1 = t4")      
            else:
                print("    t1 = int to float id3")
                print("    t2 = t1 * t1")
                print("    t3 = t2 +",v)
                print("    id1 = t3")


# In[41]:


def code_optimizer():
    print('code optimizer : ')
    if t == 3:
        if zeko == 0:
            print("    t1 = "+eq[2] +" * #"+v)
            print("    id1 = t1 + "+eq[1])
        elif zeko == 1:
            print("    t1 = #"+eq[2] +" *",v)
            print("    id1 = t1 + #"+eq[1])
    elif t == 2:
        if zeko == 0:
            print("    t1 = "+eq[3] +" * #"+v)
            print("    id1 = t1 + "+eq[1])
        elif zeko == 1:
            print("    t1 = #"+eq[3] +" *",v)
            print("    id1 = t1 + #"+eq[1])
    elif t == 1 :
        if zeko == 0:
            print("    t1 = int to float", v)
            print("    t2 = "+eq[2]+" * "+eq[3]+" ")
            print("    id1 = t1 + t2 ")
        elif zeko == 1:
            print("    t1 = #"+eq[2]+" * #"+eq[3]+" ")
            print("    id1 = t1 +",v)        


# In[51]:


def code_generator():
    print('code generator : ')
    if zeko == 0:
        isf=int(v) #to print int number while also print in tree float
        isf = float(isf)
        isf=str(isf)
    elif zeko == 1:
        isf = float(v)
        isf=str(isf)
    if t == 3:
        print("    LDF R1 , "+eq[2])
        print("    MULF R1 , R1 ,",isf)
        print("    LDF R2 , "+eq[1])
        print("    ADDF R2 , R2 , R1")
        print("    STRF id1 , R2 ")
    elif t == 2:
        print("    LDF R1 , "+eq[3])
        print("    MULF R1 , R1 ,",isf)
        print("    LDF R2 , "+eq[1])
        print("    ADDF R2 , R2 , R1")
        print("    STRF id1 , R2 ")
    elif t == 1 :
        print("    LDF R1 , "+eq[3])
        print("    LDF R2 , "+eq[2])
        print("    MULF R1 , R1 , R2")
        print("    ADDF R1 , R1 ,",isf)
        print("    STRF id1 , R1 ")


# In[ ]:




