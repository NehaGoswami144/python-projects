#!/usr/bin/env python
# coding: utf-8

# In[6]:


for i in range(0, 5): #for rows
   
    for j in range(0, 5): #for columns
        print("*", end="")
    print()


# In[42]:


for i in range(0,5):
    
    for j in range(5):
        print("**")
    print("*" ,end="")
   


# In[6]:


for i in range(0,6):
    
    for j in range(0,i+1):
        print("*"  ,end="")
    print("\n")


# In[11]:


for i in range(6,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print("\n")


# In[17]:


for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("\n")


# In[20]:


for i in range(6,0,-1):
    print("\n")
    for k in range(6-i,0):
        print(" ",end="")
    for j in range(1,i+1):
        print('*',end="")


# In[27]:



for i in range (1,6):
    print("\n")
    for j in range(1,i+1):
        print("*",end="")
        if j==5:
            for k in range(5,0,-1):
                print("*",end="")


# In[40]:



for i in range(1,6):
    print("\n")
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")


# In[48]:


for i in range(6,0,-1):
    print("\n")
    for k in range(1,7-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")


# In[83]:


for i in range(1,6):
    print("\n")
    for j in range(1,7-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
        if k==5:
            for t in range(6,0,-1): 
                print("\n")
                for o in range(1,7-t):
                    print(" ",end="")
                for h in range(1,t+1):
                    print("*",end="")
                


# In[86]:


for i in range(1,6):
    print("\n")
    for j in range(1,7-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(" *",end="")
        if k==5:
            for t in range(6,0,-1): 
                print("\n")
                for o in range(1,7-t):
                    print(" ",end="")
                for h in range(1,t+1):
                    print(" *",end="")


# In[108]:


n=5
for i in range(n):
    print("\n")
    for j in range(i,n):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    for k in range(i+1):
        print("*",end=" ")
                                


# In[76]:


for i in range(4):
    print()
    for j in range(4):
        print("*",end=" ")


# In[82]:


for i in range(10):
    print()
    for k in range()
    for j in range(1,i+1):
        print("*",end="")
        


# In[ ]:




