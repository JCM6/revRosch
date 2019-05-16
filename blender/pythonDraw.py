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

#populating the standard point matrix.
for i in range(iterMax):
    x.append(random.randrange(startPoint, maxRange, stepInc))

for i in range(iterMax):
    y.append(random.randrange(startPoint, maxRange, stepInc))

for i in range(iterMax):
    z.append(random.randrange(startPoint, maxRange, stepInc))

#populating the wild point matrix
for i in range(iterMax):
    wx.append(random.randrange(startPoint, maxRange, stepInc))

for i in range(iterMax):
    wy.append(random.randrange(startPoint, maxRange, stepInc))

for i in range(iterMax):
    wz.append(random.randrange(startPoint, maxRange, stepInc))

print('matrix of pointvalues')
print(pointMtrx)    