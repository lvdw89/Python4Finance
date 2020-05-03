from newton_raphson import newton_raphson
from jordi_method import jordi_method
from newton_raphson_variable_step import newton_raphson_variable_step
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
# function to be used in  root finder


def f(x): return 2*x ** 2-x ** 3-2


# set iteration params
eps = 0.00001
max_iter = 100
x0 = 1

# constant step
dx = 0.0001
[iter_out, xn_iter, fxn_iter, dfxn_iter] = newton_raphson(
    f, x0, dx, eps, max_iter)

# [iter_out1, xn_iter1, fxn_iter1, dfxn_iter1] = jordi_method(
# f, x0, dx, eps, max_iter)


plt.figure(1)
plt.plot(iter_out, fxn_iter, label="fxn - NR")
plt.xlabel('Nr of iterations [-]')
plt.ylabel('[-]')
plt.legend(bbox_to_anchor=(0.8, 0.2), loc='upper left', borderaxespad=0.)
plt.show()
