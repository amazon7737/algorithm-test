#!/usr/bin/env python
# coding: utf-8

# In[1]:


#11722


# In[59]:


n = int(input())


# In[3]:


a = list(map(int, input().split()))


# In[28]:


dp = [1] *n


# In[29]:


temp = 0


# In[30]:


for i in range(a.index(max(a))+1, n):
    for j in range(i):
        if a[a.index(max(a))] > a[j]:
            if temp == a[j]:
                pass
            else:
                dp[i] += 1
                temp = a[j]
        


# In[31]:


dp


# In[32]:


print(max(dp))


# In[33]:


#2579


# In[35]:


b = []


# In[34]:


n = int(input())


# In[36]:


for _ in range(n):
    b = int(input())
    a.append(b)


# In[37]:


dp = [1] * n


# In[38]:


dp[0] = a[0]


# In[39]:


dp[1] = a[0] + a[1]


# In[40]:


dp[2] = max(a[1]+a[2] , a[0] + a[2])


# In[41]:


for i in range(n):
    for j in range(1, i):
        dp[i] = max(a[0] + a[j] + a[i], a[j] + a[i])


# In[42]:


dp


# In[47]:


#2579 답


# In[1]:


n = int(input())


# In[8]:


a = [] *n


# In[9]:


dp = [0]*n


# In[10]:



for _ in range(n):
    b = int(input())
    a.append(b)


# In[11]:


if n>=3:
    dp[0] = a[0]
    dp[1] = a[0] + a[1]
    dp[2] = max(a[0] + a[2], a[1] + a[2])
    
    for i in range(3, n):
        dp[i] = max(a[i-1] + dp[i-3] + a[i] , dp[i-2], a[i])
        # max(직전칸의 값 + 3개 전계단의 최댓값 + 현재값, 2개 전 계단의 최댓값 + 현재값)
        
    print(dp[-2])

else:
    if n==1: print(a[0])
    elif n==2: print(a[0] + a[1])
    elif n==3: print(max(a[0] + a[2] , a[1] + a[2]))
        


# In[7]:


a


# In[12]:


#경우 나눠서 다시 생각해보기


# In[13]:


#1699


# In[39]:


a = int(input())


# In[40]:


dp = [0] * a


# In[41]:




if a%2==0:
dp[0] +=1
a = a-2
elif a%3==0:
dp[0] +=1
a = a-3
else:
a= a-1


# In[42]:


a


# In[43]:


dp


# In[44]:


#어렵다..


# In[45]:


n = int(input())


# In[46]:


dp = [0 for i in range(n+1)]


# In[48]:


square = [i * i for i in range(1, 317)]


# In[49]:


for i in range(1, n+1):
    s = []
    for j in square:
        if j> i:
            break
        s.append(dp[i-j])
    dp[i] = min(s) + 1
print(dp[n])


# In[50]:


for i in range(1, n+1):
    s = []
    for j in square:
        if j> i:
            break
        s.append(dp[i-j])
    dp[i] = min(s) + 1
print(dp[n])


# In[52]:


for i in range(1, n+1):
    s = []
    for j in square:
         if j> i:
                break
        s.append(dp[i-j])
    dp[i] = min(s) + 1
print(dp[n])


# In[53]:


for i in ragne(1, n+1):
    s = []
    for j in square:
        if j> i:
            break
        s.append(dp[i-j])
    dp[i] = min(s) + 1
print(dp[n])


# In[ ]:


for i in range(1, n+1):
    s = []
    for j in square:
        if j> i:
            break
        s.append()

