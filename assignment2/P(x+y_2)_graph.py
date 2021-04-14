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
Z = ( X * 0) + (Y * 0)
#

for i in range(50):
  for j in range(50):
    if X[i][j]+Y[i][j]<(1/2):
      Z[i][j]=2
    else:
      Z[i][j]=0


ax1.set_title('P(X+y)<1/2')
ax1.plot_surface(X,Y,Z)
#,cmap='viridis',edgecolor='none'

plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0,1)
plt.ylim(0,1)
#plt.xscale()
#plt.xticks()
plt.xticks(np.arange(0, 1, 0.1))
plt.yticks(np.arange(0, 1, 0.1))

plt.show()