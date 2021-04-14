import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111, projection='3d')

n=0.01

x = np.arange(0,0.5,n)
y = np.arange(0,0.5,n)
X,Y = np.meshgrid(x,y)

#creating array for storing Z values
Z = 2 + ( X * 0) + (Y * 0)

for i in range(50):
  for j in range(50):
    if X[i][j]+Y[i][j]<(1/2):
      Z[i][j]=2
    else:
      Z[i][j]=0


ax1.set_title('f(x,y)')
ax1.plot_surface(X,Y,Z,cmap='viridis',edgecolor='none')

plt.xlabel("X")
plt.ylabel("Y")


plt.show()