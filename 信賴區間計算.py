import scipy.stats as st
import numpy as np
#假設信賴區間設定為95%  我們規劃一個函數來處理
def ci(data,confidence=0.95):
    #計算時會有浮點數 可先將數值資料計算成浮點數
    a=1.0*np.array(data)
    n=len(a)
    m=np.mean(a) #平均值
    se=st.sem(a) #標準差
    h=se*st.t.ppf((1+confidence)/2.,n-1)
    return m,m-h,m+h
sample1=[50,60,70,80,40,64,55,88,99,25] #樣本資料
a,b,c=ci(sample1)
print(a)
print(b)
print(c)


