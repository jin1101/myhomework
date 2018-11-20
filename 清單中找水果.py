a=input('請輸入喜歡的水果:')
list=['香蕉','芒果','草莓','蘋果','西瓜']
while len(a) > 0:
    if a not in list:
        print(a+'不在list清單中')
    else:
        b=list.index(a)
        print(a+'在list清單中中的第'+str(b+1)+'項')
    a=input('請輸入喜歡的水果:')