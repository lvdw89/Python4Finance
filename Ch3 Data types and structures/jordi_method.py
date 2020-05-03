def jordi_method(f, x0, dx, epsilon, max_iter):
    iter_out = []
    xn_iter = []
    fxn_iter = []
    dfxn_iter = []

    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        dfxn = (f(xn+dx)-f(xn))/dx
        if (abs(fxn) < epsilon):
            print('sol found, xn= {:f}' .format(xn))
            # no root has been found, update estimate
        xn = xn-dfxn
        # return something regardless
        iter_out.append(n)
        xn_iter.append(xn)
        fxn_iter.append(fxn)
        dfxn_iter.append(dfxn)
    return iter_out, xn_iter, fxn_iter, dfxn_iter
