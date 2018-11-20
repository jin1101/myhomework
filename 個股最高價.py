import numpy as np
import pandas as pd
df=pd.read_csv('./data/stockQuote_all.csv')
#df.SymbolId = df.SymbolId + ' ' + df.SymbolName
df2=df[['QuoteDate','SymbolId', 'ClosePrice']]
df.head()
# create pivot table
pivot_table=df2.pivot_table('ClosePrice', index='QuoteDate', columns='SymbolId')
pivot_table.head()
pivot_table.columns
pivot_table.index
# 台積電最高價發生的日期
highest_date = pivot_table['2330'].idxmax()
highest_date
pivot_table.loc[highest_date, ['2330']][0]
highest_list = []
for symbol_id in pivot_table.columns:
    highest_date = pivot_table[symbol_id].idxmax()
    highest_price = pivot_table.loc[highest_date, [symbol_id]][0]
    highest_list += [[symbol_id, highest_date, highest_price]]
#highest_list=pd.DataFrame(highest_list)
highest_list[0]
df_highest=pd.DataFrame(highest_list, columns=['SymbolId', 'highest_date', 'highest_price'])
df_highest.head()
df_highest.shape
# find all id with names
id_name = df[['SymbolId', 'SymbolName']].drop_duplicates()
# 依共同的欄位名稱(SymbolId) join
res = pd.merge(id_name, df_highest, on='SymbolId')
res