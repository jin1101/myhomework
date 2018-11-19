a=input('請輸入身高，單位為公分:')
b=input('請輸入體重，單位為公斤:')
c=float(b)/(float(a)/100)**2
if c<18.5:
    print('your BMI is', c, '您的體重過輕')
elif c>=18.5 and c<25:
    print('your BMI is', c, '您的體重正常')
elif c>=25 and c<30:
    print('your BMI is', c, '您的體重過重')
else:
    print('your BMI is', c, '您的體重肥胖')