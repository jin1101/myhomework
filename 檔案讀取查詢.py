import pandas as pd
import numpy as np
data=pd.read_csv('https://quality.data.gov.tw/dq_download_csv.php?nid=5958&md5_url=7679aa8d28f1d3cdecd9b596d124e92a')
a=np.array(data.iloc[0:,0:1])
c=np.array(data.iloc[0:,1:2])
d=np.array(data.iloc[0:,3:4])
b=np.array(data.iloc[0:,2:3])
n=0
number=int(input('郵遞區號查詢派出所\n請輸入郵遞區號：'))
for x in b:
    if x ==number:
        print('分局名稱（中文）：',a[n],'\t','分局名稱（英文）：',c[n],'\t','地址：',d[n])
    n+=1