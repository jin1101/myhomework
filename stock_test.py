import pandas as pd
df = pd.read_csv('2330.csv',encoding="utf-8")
df.head()
df["QuoteDate"] = pd.to_datetime(df['QuoteDate'])
df.head()
df.ClosePrice.max()
df.ClosePrice.argmax()
df.QuoteDate[99]
df.iloc[99]
m=df.set_index('QuoteDate').resample('M')["ClosePrice"].mean( )
q=df.set_index('QuoteDate').resample('Q')["ClosePrice"].mean( )
m
%matplotlib inline
df.plot('QuoteDate', 'ClosePrice')
m.plot()
q.plot()
df.plot('QuoteDate', 'ClosePrice')