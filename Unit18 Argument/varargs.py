def tracer(ff, *pargs, **kargs):
    print("calling: ", ff.__name__)
    return ff(*pargs, **kargs)


def func(a, b, c, d):
    return a+b+c+d

print(tracer(func, 1, 2, c=3, d=4))
