import matplotlib.pyplot as plt
import numpy as np
'''
x+y=9  ->
y=9-x

5a+15b=75 ->
15b=75-5a
3b=15-a

b=5-0.3a
y=x^2+2x+2
 
'''
x1=np.linspace(-10,10,25)
print(x1)
x3=x2=x1
y1=9-x1
y2=5-0.3*x2
y3=x3**2+2*x3+2
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.grid()
plt.show()