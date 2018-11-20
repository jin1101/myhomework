%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('https://quality.data.gov.tw/dq_download_csv.php?nid=21115&md5_url=79a3f885752aa3d16a9a5eda4683770c')
df.head()
df3=df.drop(["交流道","進出口","週2-4"],axis=1)
df3.head()
df4 = df3.groupby("路線方向").sum()
df4.head()
df5=df4[(df4["週六"]>2000000) & (df4["週日"] > 2000000)]
df5
df5.index=df5.index.str.replace("國1北向路段","1北向")
df5.index=df5.index.str.replace("國1南向路段","1南向")
df5.index=df5.index.str.replace("國3北向路段","3北向")
df5.index=df5.index.str.replace("國3南向路段","3南向")
print(df5.index)
df5.plot.bar()
plt.xlabel("路線編號")
plt.ylabel("車流量")
plt.show()
