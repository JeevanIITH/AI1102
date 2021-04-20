import numpy as np 
import random
import math

#creating x points from -1 to 1
x=np.linspace(-1,1,10000)

#creating y points from -1 to 1
y=np.linspace(-1,1,10000)

#sample space
sample=1000

#intialization of count for number of favorable outcomes
count=0

#performing the event for 10000 times
for i in range(10000):
    #choosing a random point from x points
    random_num_x=random.choice(x)
    
    #choosing a random point from y points
    random_num_y=random.choice(y)
    
    #checking favorable outcome i.e., max(x,y)< 1/2
    if(max(random_num_x,random_num_y)<(1/2)):
        #increament of count of favorable outcomes
        count=count + 1
      

#probability = (no of favourable outcomes)/(total no of outcomes)
probability_sim= (count)/10000    
#print(probability)

print("Theoritical probability is ",(9/16))
print("Simulated probability is ", probability_sim)
print("Absolute Error between them is ",abs(probability_sim-(9/16)),"Which is neglegible") 
print("So we can conclude P[max(x,y)< 1/2]=",9/16)   