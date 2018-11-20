a=input("發票:")
b=round(int(a)/1.05)
c=int(a) - b
print('商品未稅價\t',b,'元')
print('加值稅    \t',c,'元')
print('----------------------------')
print('總價      \t',b+c,'元')
