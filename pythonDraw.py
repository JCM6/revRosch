import math
import random

#define iterations
iterMax = 5
iterCount = 0

#define base components
x = []
y = []
z = []

#wildcard modifiers
wx = []
wy = []
wz = []

#component matricies
pointMtrx = [x], [y], [z]
wildPointMtrx = [wx], [wy], [wz]


for i in range(iterMax):
    x.append(random.randrange(1, 10, 1))
print(x)
print(pointMtrx)    