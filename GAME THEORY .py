#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import random
from numpy.random import normal
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
import warnings
warnings.filterwarnings("ignore")


# in the  cournot duopoly model we are solving on the competition of two companies over quantity.let q1,q2 be the respective quantities."a" be a constant .we will first deploy the standard cournot function then try some other functions and check their reliability.

# In[7]:


#c1=c2
allq1=[]
allq2=[]
allprofit1=[]
allprofit2=[]
notimes=int(input("enter the no of time: "))
for i in range(notimes):
  quantities=[random.uniform(100,2000) for i in range(2)]
  q1=int(quantities[0])
  q2=int(quantities[1])
  allq1.append(q1)
  allq2.append(q2)
  total=(q1+q2)
  a=4001
  c1=500
  c2=500
  quant=[q1,q2]
  profits=[(a-total-c1)*q1,(a-total-c2)*q2]
  allprofit1.append(profits[0])
  allprofit2.append(profits[1])
  print(f"for the quantities:{(quant)} the profits are :{profits}")
allq1sort=np.sort(allq1)
allprof1graph=[]
for i in range(notimes):
    indexfetch=allq1.index(allq1sort[i-1])
    allprof1graph.append(allprofit1[indexfetch])
plt.plot(allq1sort,allprof1graph,marker='o',linestyle='-',color='r')
plt.xlabel('quantity(q1)')
plt.ylabel('profits(profits[0])')
plt.title('profit vs quantity for company1')
plt.show
maxquantitytheo=((a-c1)/3)
print(f"the theoretical quantity for maximum profit is{maxquantitytheo}")
max_profit_company1=max(allprofit1)
maxprofitindex=allprofit1.index(max_profit_company1)
max_profit_quantity1=allq1[maxprofitindex]
print(f"\n\nthe maximum profit achieved by company 1 is  is:{max_profit_company1} and the quantity corrs is :{max_profit_quantity1}.")
max_profit_company2=max(allprofit2)
maxprofitindex2=allprofit2.index(max_profit_company2)
max_profit_quantity2=allq2[maxprofitindex2]
print(f"the maximum profit achieved by company 2 is  is:{max_profit_company2} and the quantity corrs is :{max_profit_quantity2}.")


# In[9]:


allq2sort=np.sort(allq2)
allprof2graph=[]
for i in range(notimes):
    indexfetch=allq2.index(allq2sort[i-1])
    allprof2graph.append(allprofit2[indexfetch])
print(f"the maximum profit achieved by company 2 is  is:{max_profit_company2} and the quantity corrs is :{max_profit_quantity2}.")
plt.plot(allq2sort,allprof2graph,marker='o',linestyle='-',color='b')
plt.xlabel('quantity(q2)')
plt.ylabel('profits(profits[1])')
plt.title('profit vs quantity for company2')
plt.show


# in  the above case we have considered an equal operatioal cost that is c1=c2.you can see the maximuum profit for the comapany 1 and its corresponding quantity in the text just above the graph for company 1. below it you can see the same for the company  two . since c1=c2, for the maximum profit the quantities corresponding should be equal.if you consider  lower no of rounds you may not find that the quantitites corresponding to max profit to be equal since we are using the random function .so use the no o0f times like 1000 and see the difference with the lower no of times.

# In[11]:


#for randomly generated a and c.exact meaning and shape are shown in higer no of time like 1000
allq1=[]
allq2=[]
allprofit1=[]
allprofit2=[]
notimes=int(input("enter the no of time: "))
for i in range(notimes):
  quantities=[random.uniform(100,2000) for i in range(2)]
  q1=int(quantities[0])
  q2=int(quantities[1])
  allq1.append(q1)
  allq2.append(q2)
  total=(q1+q2)
  ac=[random.randint(400,4000) for _ in range(2)]
  ac[0]=a
  ac[1]=c1
  c1=c2
  quant=[q1,q2]
  profits=[(a-total-c1)*q1,(a-total-c2)*q2]
  allprofit1.append(profits[0])
  allprofit2.append(profits[1])
  print(f"for the quantities:{(quant)} the profits are :{profits}")
allq1sort=np.sort(allq1)
allprof1graph=[]
for i in range(notimes):
    indexfetch=allq1.index(allq1sort[i-1])
    allprof1graph.append(allprofit1[indexfetch])
plt.plot(allq1sort,allprof1graph,marker='o',linestyle='-',color='r')
plt.xlabel('quantity(q1)')
plt.ylabel('profits(profits[0])')
plt.title('profit vs quantity for company1')
plt.show
maxquantitytheo=((a-c1)/3)
print(f"the theoretical quantity for maximum profit is{maxquantitytheo}")
max_profit_company1=max(allprofit1)
maxprofitindex=allprofit1.index(max_profit_company1)
max_profit_quantity1=allq1[maxprofitindex]
print(f"\n\nthe maximum profit achieved by company 1 is  is:{max_profit_company1} and the quantity corrs is :{max_profit_quantity1}.")
max_profit_company2=max(allprofit2)
maxprofitindex2=allprofit2.index(max_profit_company2)
max_profit_quantity2=allq2[maxprofitindex2]
print(f"the maximum profit achieved by company 2 is  is:{max_profit_company2} and the quantity corrs is :{max_profit_quantity2}.")


# In[53]:


#c1>c2
allq1=[]
allq2=[]
allprofit1=[]
allprofit2=[]
notimes=int(input("enter the no of time: "))
for i in range(notimes):
  quantities=[random.uniform(100,2000) for i in range(2)]
  q1=int(quantities[0])
  q2=int(quantities[1])
  allq1.append(q1)
  allq2.append(q2)
  total=(q1+q2)
  a=4000
  c1=1000
  c2=100
  quant=[q1,q2]
  profits=[(a-total-c1)*q1,(a-total-c2)*q2]
  allprofit1.append(profits[0])
  allprofit2.append(profits[1])
  print(f"for the quantities:{(quant)} the profits are :{profits}")
allq1sort=np.sort(allq1)
allprof1graph=[]
for i in range(notimes):
    indexfetch=allq1.index(allq1sort[i-1])
    allprof1graph.append(allprofit1[indexfetch])
plt.plot(allq1sort,allprof1graph,marker='o',linestyle='-',color='r')
plt.xlabel('quantity(q1)')
plt.ylabel('profits(profits[0])')
plt.title('profit vs quantity for company1')
plt.show
max_profit_company1=max(allprofit1)
maxprofitindex=allprofit1.index(max_profit_company1)
max_profit_quantity1=allq1[maxprofitindex]
print(f"the maximum profit achieved by company 1 is  is:{max_profit_company1} and the quantity corrs is :{max_profit_quantity1}.")
max_profit_company2=max(allprofit2)
maxprofitindex2=allprofit2.index(max_profit_company2)
max_profit_quantity2=allq2[maxprofitindex2]
print(f"the maximum profit achieved by company 2 is  is:{max_profit_company2} and the quantity corrs is :{max_profit_quantity2}.")


# In[13]:


allq2sort=np.sort(allq2)
allprof2graph=[]
for i in range(notimes):
    indexfetch=allq2.index(allq2sort[i-1])
    allprof2graph.append(allprofit2[indexfetch])
print(f"the maximum profit achieved by company 2 is  is:{max_profit_company2} and the quantity corrs is :{max_profit_quantity2}.")
plt.plot(allq2sort,allprof2graph,marker='o',linestyle='-',color='b')
plt.xlabel('quantity(q2)')
plt.ylabel('profits(profits[1])')
plt.title('profit vs quantity for company2')
plt.show


# in  the above case we have considered an unequal operational efficiency that is c1=1000,c2=100.you can see the maximuum profit for the company 1 and its corresponding quantity in the text just above the graph for company 1. below it you can see the same for the company 2 . the next graph is for company 2.

# now in the next case we take function such that if the quantity is zero then price infinite and if the quantity is infinite price is some constant.

# In[15]:


#c1=c2
allq1=[]
allq2=[]
allprofit1=[]
allprofit2=[]
notimes=int(input("enter the no of time: "))
for i in range(notimes):
  quantities=[random.uniform(100,2000) for i in range(2)]
  q1=int(quantities[0])
  q2=int(quantities[1])
  allq1.append(q1)
  allq2.append(q2)
  total=(q1+q2)
  a=4000
  c1=100
  c2=100
  quant=[q1,q2]
  ex=(2000-(total))/(total)
  multi=np.exp(ex)
  profits=[((a*multi)-c1)*q1,((a*multi)-c2)*q2]
  allprofit1.append(profits[0])
  allprofit2.append(profits[1])
  print(f"for the quantities:{(quant)} the profits are :{profits}")
allq1sort=np.sort(allq1)
allprof1graph=[]
for i in range(notimes):
    indexfetch=allq1.index(allq1sort[i-1])
    allprof1graph.append(allprofit1[indexfetch])
plt.plot(allq1sort,allprof1graph,marker='o',linestyle='-',color='r')
plt.xlabel('quantity(q1)')
plt.ylabel('profits(profits[0])')
plt.title('profit vs quantity for company1')
plt.show
max_profit_company1=max(allprofit1)
maxprofitindex=allprofit1.index(max_profit_company1)
max_profit_quantity1=allq1[maxprofitindex]
print(f"\n\nthe maximum profit achieved by company 1 is  is:{max_profit_company1} and the quantity corrs is :{max_profit_quantity1}.")
max_profit_company2=max(allprofit2)
maxprofitindex2=allprofit2.index(max_profit_company2)
max_profit_quantity2=allq2[maxprofitindex2]
print(f"the maximum profit achieved by company 2 is  is:{max_profit_company2} and the quantity corrs is :{max_profit_quantity2}.")


# In[17]:


allq2sort=np.sort(allq2)
allprof2graph=[]
for i in range(notimes):
    indexfetch=allq2.index(allq2sort[i-1])
    allprof2graph.append(allprofit2[indexfetch])
print(f"the maximum profit achieved by company 2 is  is:{max_profit_company2} and the quantity corrs is :{max_profit_quantity2}.")
plt.plot(allq2sort,allprof2graph,marker='o',linestyle='-',color='b')
plt.xlabel('quantity(q2)')
plt.ylabel('profits(profits[1])')
plt.title('profit vs quantity for company2')
plt.show


# this could also be a reliable function.but with one expection.here from the graph we can observe that the average profit is constantly increasing with quantity.and the quantities corresponding to maximum profit are obtaines in the middle using the same cournot model

# NOW WE ARE WORKING UPON THE BERTRAND MODEL .WHICH IS THE COMPETITON OVER PRICE.WE GENERALLY HAVE THREE CASES.1)if p1>p2 all customers buy from 2 then firm 1 cannot make any profit.2)if p1<p2 all customers buy from 1 then firm 2 makes no profit . and the thrid case is that the both firms have the equal pricing additionally we are taking a probablility factor for the selction by the customer in between firm1 and firm 2.initially we are considering equal operationalcost then after unequal

# In[19]:


#c1=c2
allprob1=[]
allprob2=[]
allprofit1=[]
allprofit2=[]
notimes=int(input("enter the no of time: "))
for i in range(notimes):
  a1=random.uniform(0,1)
  proba=[a1,(1-a1)]
  a1=proba[0]
  a2=proba[1]
  allprob1.append(a1)
  allprob2.append(a2)
  price=4000
  c1=2000
  c2=2000
  profits=[(a1*(price-c1)),(a2*(price-c2))]
  allprofit1.append(profits[0])
  allprofit2.append(profits[1])
  print(f"for the probabilities:{(proba)} the profits are :{profits}")
allprob1sort=np.sort(allprob1)
allprof1graph=[]
for i in range(notimes):
    indexfetch=allprob1.index(allprob1sort[i-1])
    allprof1graph.append(allprofit1[indexfetch])
plt.plot(allprob1sort,allprof1graph,marker='o',linestyle='-',color='r')
plt.xlabel('probability(a1)')
plt.ylabel('profits(profits[0])')
plt.title('profit vs probability of customer choosing for company1')
plt.show
max_profit_company1=max(allprofit1)
maxprofitindex=allprofit1.index(max_profit_company1)
max_profit_prob1=allprob1[maxprofitindex]
print(f"\n\nthe maximum profit achieved by company 1 is  is:{max_profit_company1} and the prob corrs is :{max_profit_prob1}.")
max_profit_company2=max(allprofit2)
maxprofitindex2=allprofit2.index(max_profit_company2)
max_profit_quantity2=allprob2[maxprofitindex2]
print(f"the maximum profit achieved by company 2 is  is:{max_profit_company2} and the prob corrs is :{max_profit_quantity2}.")


# In[21]:


allprob2sort=np.sort(allprob2)
allprof2graph=[]
for i in range(notimes):
    indexfetch=allprob2.index(allprob2sort[i-1])
    allprof2graph.append(allprofit2[indexfetch])
print(f"the maximum profit achieved by company 2 is  is:{max_profit_company2} and the prob corrs is :{max_profit_quantity2}.")
plt.plot(allprob2sort,allprof2graph,marker='o',linestyle='-',color='b')
plt.xlabel('probability(a2)')
plt.ylabel('profits(profits[1])')
plt.title('profit vs probability for company2')
plt.show


# we have got the exact graph as shownn in the bertrand model . as the probability of the customer choice for a specitfic firm increases its profit incrases here as the price and the operational cost is same.THE OPTIMAL SITUATION FOR  BOTH THE COMPANIES IN THIS CASE IS TO HAVE A EQUAL SPLIT THAT IS 0.5 PROBABILITY FOR EACH TO HAVE SAME PROFIT INSTEAD OF COMPETING AGAIN ON TO EITHER SIDES OF MOVING TO MONOPLOY OR PRICE=0. WE CAN ALSO OBSERVE THESE GRAPHS AND RELATE WITH THE MODEL WHERE IT SAID THAT THE MAXIMUM PROFIT IS ACHIEVED AT THE MONOPOLYT WHICH THRE PROBABILITY IS EQUAL TO 1.

# In[ ]:




