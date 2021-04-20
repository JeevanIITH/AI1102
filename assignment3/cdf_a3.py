import numpy as np
from matplotlib import pyplot as plt
import math

x=np.linspace(-1,1,10000)

F_x= (1/2)*(x+1)


plt.xlabel("X")
plt.ylabel("F(x)")
plt.title("CDF")

plt.plot(x,F_x)
plt.show()

