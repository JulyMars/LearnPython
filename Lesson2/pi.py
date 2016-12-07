#pi.py
from random import random
from math import sqrt
from time import clock

DARTS = 2**10
hits = 0
clock()

for i in range(1,DARTS):
	x,y = random(),random()
	dist = sqrt(x**2 + y**2)
	if dist <= 1.0:
		hits = hits+1
pi = hits * 4.0 / DARTS

print("pi: %s"%pi)
print("time %-5.5ss"%clock())