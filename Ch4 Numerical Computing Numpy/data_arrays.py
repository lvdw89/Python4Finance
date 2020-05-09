# Python array class

#  - > lists are essentially arrays if the same data type is used
import math
import timeit
import numpy as np

v = [0.5, 0.75, 0.9, 3]
# list can contain multiple datatype , so multiple list object can be combined in a new list m
m = [v, v, v]
print(m[0][2])

v[0] = 'Python'
print(m)

# use purpose built numpy data array
a = np.array([0, 21, 34, 4, 5, 3])
print(a.sum())

b = np.array([a, a*2])
print(b)
print(b[1, 2])
print(b.sum(axis=0))
print(b.sum(axis=1))


c = np.zeros((3, 3))
print(c)
