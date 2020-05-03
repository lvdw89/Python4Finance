import decimal
from decimal import Decimal

decimal.getcontext().prec = 300
d = Decimal(1)/Decimal(11)
print(d)


print(bool(1))

a = 'this is an integer {:.2f}'.format(2)
print(a)

i = 0

while i < 3:
    print('i is {:d}'.format(i))
    i += 1

# tuple
t = 1, 2, 'data'
print(type(t))
print(t[0])
# only allows count and index
print(t.count('data'))  # counts occurences of data
print(t.index(1))  # find index where 1 occurs

l = [1, 2, 'daat']
print(l[2])
t = list(t)
la = [0, 1, 2, 3, 4, 5, 6, 7]
print(la[0:6:2])  # print every 2nd index from index 0 to 6-1

for element in la[3:5]:  # list based looping
    print(element**2)

for bla in range(0, 4):  # counter based
    print(bla)

m = [2*i for i in range(4)]  # generate list through looping
print(m)


def f(x):
    return x**2


print(f(3))


def even(x):
    return x % 2 == 0


t = range(10)
# apply even function to whole list t and save results in list
bla = list(map(even, t))
print(bla)

# pass function def directly into map
bla = list(map(lambda x: x**2, range(10)))
print(bla)

d = set(['u', 'd', 'ud', 'du', 'd', 'du'])
print(d)
