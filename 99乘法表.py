i=0
j=0
for i in range(1,10):
    a=''
    for j in range(1,10):
        a+=str(i)+"*"+str(j)+"="+str(i*j)+"\t"
    print(a)