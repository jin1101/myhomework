x=input('input string:')
x[::-1]
''.join(reversed(x))
if x == x[::-1]:
    print("OK")
else:
    print('Error')