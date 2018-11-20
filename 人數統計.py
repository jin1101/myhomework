import pandas as pd
import numpy as np
data=pd.read_csv('http://opendataap2.penghu.gov.tw/./resource/files/2018-08-01/5a57d0a9729568b778934dc37c4e3391.csv')
a=np.array(data.iloc[:19,0:1])
a=a.reshape(1,19)
b=np.array(data.iloc[:19,1:2])
b=b.reshape(1,19)
c=np.array(data.iloc[:19,3:4])
d=np.array(data.iloc[:19,4:5])
c=np.add(c,d)
c=c.reshape(1,19)
n=0
while n>=0 and n<19:
    print(a[0,n],b[0,n],'\t',"國小（含）之前的人數：",c[0,n])
    n+=1