from collections import Callable

class Power1(Callable):
    def __call__(self, x, n):
        p = 1
        for i in range(n):
            p *= x
        return p

class Power4(Callable):
    def __call__(self, x, n):
        if n == 0: return 1

        elif n % 2 == 1:
            return self.__call__(x,n-1) * x

        else:  # n % 2 ==0:
            t = self.__call__(x, n//2)
            return t*t


import timeit
pow1= Power1()
iterative= timeit.timeit(
"pow1(2,1024)",
"""
from collections import Callable
class Power1(Callable ):
    def __call__( self, x, n ):
        p= 1
        for i in range(n):
            p *= x
        return p
pow1= Power1()
""",
number=100000 ) # otherwise it takes 3 minutes

print( "Iterative", iterative )