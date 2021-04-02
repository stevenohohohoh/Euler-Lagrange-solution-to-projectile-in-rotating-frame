import math
import matplotlib.pyplot as plt
import numpy as np

r = 1
v = -2
omega = 1
c = 1

def x_position(t):
    d = (r*math.sin(omega*t)*t*c) + (r*math.cos(omega*t)) + (math.cos(omega*t)*v*t)
    return d
    
def y_position(t):
    d = ((math.cos(omega*t)*r*c) - (math.sin(omega*t))*v)*t - (math.sin(omega*t)*r)
    return d

array_x = []
array_y = []

noninertial_x = []
noninertial_y = []

total = (r*math.sqrt(2))/abs(v)
print(total)

for i in np.arange(0.0000, 1, 0.0001):
    noninertial_x.append(r-i)
    noninertial_y.append(i)
    if (math.pow(x_position(i), 2)+math.pow(y_position(i), 2)) < math.pow(r, 2):
        array_x.append(x_position(i))
        array_y.append(y_position(i))

print(math.sqrt(math.pow(array_x[(len(array_x)/2)], 2) + math.pow(array_y[(len(array_y)/2)], 2)) )
fig, ax = plt.subplots()
ax.add_patch(plt.Circle((0, 0), r, color='#cccccc', alpha=0.5))
ax.set_aspect('equal', adjustable='datalim')
ax.plot() 
plt.ylim(-r, r)
plt.xlim(-r,r)
plt.plot(array_x[(len(array_x)/2)], array_y[(len(array_y)/2)], 'g*')
plt.plot(array_x, array_y)
plt.plot(noninertial_x, noninertial_y)
plt.show()


