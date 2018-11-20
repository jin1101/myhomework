import numpy as np
import stats as sts
a = [31, 24, 23, 25, 14, 25, 13, 12, 14, 23,
          32, 34, 43, 41, 21, 23, 26, 26, 34, 42,
          43, 25, 24, 23, 24, 44, 23, 14, 52,32,
          42, 44, 35, 28, 17, 21, 32, 42, 12, 34]
scores=np.array(a)
print('總合為：',np.sum(scores))
print('筆數為：',len(scores))
print('平均值為:',np.mean(scores))
print('中位數為:',np.median(scores))
print('眾數為:',sts.mode(scores))
print('上四分位數為',sts.quantile(scores,p=0.25))
print('下四分位數為',sts.quantile(scores,p=0.75))
print('最大值:',np.max(scores))
print('最小值:',np.min(scores))
print('全距:',np.ptp(scores))
print('標準差:',np.std(scores))
print('變異數:',np.var(scores))
print('離散係數:',np.std(scores)/np.mean(scores))
print('偏態係數:',sts.skewness(scores))
print('峰態係數:',sts.kurtosis(scores))