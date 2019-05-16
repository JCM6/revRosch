import math
import random

#define iterations
iterMax = 5
iterCount = 0

#define bounds
maxRange = 10
stepInc = 1
startPoint = 0


#define base components
x = []
y = []
z = []

#wildcard modifiers
wx = []
wy = []
wz = []

#component matricies
pointMtrx = [x, y, z]
wildPointMtrx = [wx], [wy], [wz]

#define scene collection



for i in range(iterMax):
    x.append(random.randrange(startPoint, maxRange, stepInc))

for i in range(iterMax):
    y.append(random.randrange(startPoint, maxRange, stepInc))

for i in range(iterMax):
    z.append(random.randrange(startPoint, maxRange, stepInc))

print('matrix of pointvalues')
print(pointMtrx)    