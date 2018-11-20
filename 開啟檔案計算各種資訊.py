import pandas as pd
import numpy as np
aap=pd.read_csv("./aapl.csv",usecols=(4,5))
vol=aap["Volume"]
clo=aap["Close"]
print('收盤價最大值:',clo.max())
print('收盤價最小值:',clo.min())
print('收盤價平均值:',clo.mean())
print('收盤價中位數:',clo.median())
ave=np.average(np.array(clo),weights=vol)
print('收盤價全平均值:',ave)