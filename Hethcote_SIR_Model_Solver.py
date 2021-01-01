#!/usr/bin/env python
# coding: utf-8

# # Numerical Estimation for the generalized SIR Model

# In[99]:


#Autor: Imelda Trejo 
#Sep 05,2020


# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats  
from scipy.stats import lognorm
from scipy.stats import expon


# In[12]:


#Integral-differential equation solver
#Trapezoidal approximation for the integral
def GenModel (I0,n,b,F,N,p):
    DS=np.zeros(n)
    S=np.zeros(n)
    I=np.zeros(n)
    #initial conditions
    I[0]=p*I0;  
    S[0]=N-I[0];
    DS[0]=-b*I[0]*S[0]/(N*p)+b*(1-p)*I[0]/p;
    S[1]=S[0]+DS[0]*h
    I[1]=(1-F[1])*(I[0]-h*DS[0])
    DS[1]=-b*I[1]*S[1]/(N*p)+b*(1-p)*I[1]/p;
    for i in range(1,n-1):
        sum=0 
        for j in range(1,i):
            sum=sum-DS[j]*(1-F[i+1-j])*h
        S[i+1]=S[i]+DS[i]*h   
        I[i+1]=I[0]*(1-F[i+1])-h*(DS[0]*(1-F[i+1])+3*DS[i]*(1-F[1]))/2+sum
        DS[i+1]=-b*I[i+1]*S[i+1]/(N*p)+b*(1-p)*I[i+1]/p  
    dydt=[S,I]
    return dydt


# In[60]:


#--integration variables:
n=800        #Observed period
Delta=1     #window size=days
h=0.1       #step size of intergation
tf=Delta*n  #Elapsed time 
tp=int(tf/h)+1  #total of points
t=np.zeros(tp)
a=int(Delta/h)
for i in range(1,tp):
    t[i]=h*i
#-----Epidemics parameter values
N=20000000
b=1/8
p=.7
I0=2
#Probability distribution function of the infectious period 
f1=expon.pdf(t,0,10)
F1=expon.cdf(t,0,10)


# In[61]:


#-----Numerical Results
SolS=GenModel(I0,tp,b,F1,N,p)
Saux,Iaux=SolS[0],SolS[1]


# In[64]:


#-----Figures
I=np.zeros(n)
for k in range(0,n):
    I[k]=Iaux[a*k]
print('Population size:',N)    
print('Initial condition:',I0) 
print('Time (days):',n)
plt.plot(I,label='p=0.7')
plt.xlabel('Time (Days)',fontsize=14)
plt.ylabel('Infectious: I(t)',fontsize=14)
plt.legend()
plt.show()


# In[ ]:




