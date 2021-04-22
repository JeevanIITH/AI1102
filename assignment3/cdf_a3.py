import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
 if(-1<x<1): return (1/2)*(x+1)
 if(x>1): return 1
 else: return 0

x = np.linspace(-2,2,10000)

y = []
for i in range(len(x)):
   y.append(f(x[i]))


plt.xlabel("X")
plt.ylabel("F(x)")
plt.title("CDF")

plt.plot(x,y)

plt.show()