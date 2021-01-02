#!/usr/bin/env python
# coding: utf-8

# # COVID-19 Data from WHO

# In[1]:


#Autor: Imelda Trejo 
#Oct 15th,2020
#COVID-19 Data from WHO where:
#----------Data are based on official laboratory-confirmed COVID-19 case and deaths reported to WHO 
#----------by country/territories/areas
#----------largely based upon WHO case definitions and surveillance guidance.


# In[2]:


# Import relevant modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


#Daily incidence cases from WHO-Covid-19 Data Set
baseURL="https://covid19.who.int/WHO-COVID-19-global-data.csv"
allDataWHO=pd.read_csv(baseURL,skipinitialspace=True)
#My Data
data=pd.read_csv("../SIR_paper_II/PopCountries.csv")
ID=np.array(data.get(["Country"])).ravel()


# In[4]:


def RdataWHO(key):
    cn=ID[key] #Country Name
    myNewData=allDataWHO.loc[allDataWHO['Country']==cn,: ]
    Yaux= np.array(myNewData.get(['New_cases'])).ravel()
    aux,cont=0,0
    while aux<1:
        if Yaux[cont]>0:
            aux=1
        cont=cont+1   
    cont=cont-1    
    Tfaux1=np.where([myNewData['Date_reported'] == '2021-01-01'])[1]
    Tfaux=Tfaux1[0]
    Ti=np.array(myNewData.get(['Date_reported'])).ravel()[cont]
    Tf=np.array(myNewData.get(['Date_reported'])).ravel()[Tfaux]
    Y=Yaux[cont:Tfaux+1] 
    #print(Yaux[260:])
    n=Y.size 
    #clean the data
    #-------Peru
    #Y[148]=Y[149]/2
    #Y[149]=Y[149]/2
    #-------Mexico
    #Y[225]=(Y[224]+Y[226])/2
    #-------Chile
    #Y[107]=(Y[106]+Y[105])/2
    #-------Ecuador
    #Y[56]=(Y[54]+Y[57])/2
    #Y[191]=(Y[190]+Y[192])/2
    #-------US
    #Y[335]=(Y[334]+Y[336])/2
    for k in range(0,n):
        if Y[k]<0:
            Y[k]=-Y[k]       
    return Y, n, Ti, Tf


# In[5]:


#US=0, Italy=1,'France'=2, 'Spain'=3 'United Kingdom'=4,'Greece'=5 'Sweden'=6 
#'Netherlands'=7, 'Belgium'=8, 'Mexico'=9, 'Chile'=10, 'Peru'=11 ,'Brazil=12' 
#'Ecuador=13' 'Argentina=14' 'Paraguay=15' 'Colombia16' 'Panama=18', 'China=19'
key=1
Y, n, tinit, tfinal =RdataWHO(key)
#print(np.argmax(Y))


# In[6]:


#----------Overage data-------------
YMV=np.zeros(n) #average movie
for k in range(3,n):
    YMV[k]=np.mean(Y[k-3:k+4]) #we may need to take integers only
YMV[0]=np.mean(Y[0:7])
YMV[1],YMV[2]=YMV[0],YMV[0]

#---Curves-Plots---
T=np.linspace(0,n,n)
fig = plt.figure(figsize=(13,4))
plt.plot(T,Y,'.',color='blue',alpha=1,label='WHO raw data')
plt.vlines(T,0,Y,color='grey',lw=2.5,alpha=.7)
plt.plot(T,YMV,'-',color='r',lw=4,alpha=.7,label="Average per 7 days");
plt.xlabel('Time (month/day/year)',fontsize=20)
plt.ylabel('Daily incidence cases ',fontsize=20)
lables=pd.date_range(start=tinit,end=tfinal,periods=12).strftime('%D')
xn=np.size(lables)
x=np.linspace(0,n,xn)
#plt.ylim(-100,2200)
plt.xticks(x, lables, rotation='vertical')
fig.autofmt_xdate()
plt.legend(loc='best') 
plt.title('%s:' % ID[key],fontsize=24)
plt.tick_params(labelsize=16)
plt.legend(fontsize=16)
fig.savefig('%sData.pdf' % ID[key])
#fig.savefig('USAData.pdf')


# In[ ]:




