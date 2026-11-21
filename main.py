import math as m


def f(a,b):
    y=m.sqrt(a/b+1)
    return y
def s(a,b):
    y=abs(a/b-1)
    return y
def t(x):
    y=m.sin(x+2)
    return y
def fo(x,b):
    y=m.tan(1+x/b)
    return y



print(f(2,7))
print(s(6,1))
print(t(43))
print(fo(6,32))