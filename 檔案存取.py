import pandas as pd
data=pd.read_csv('http://opendataap2.penghu.gov.tw/./resource/files/2017-06-08/a9ffc02d9c3e6a979a178c62772914e8.csv')
print(data.iloc[:,0:3])