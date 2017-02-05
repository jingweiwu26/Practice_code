# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 15:21:34 2017

@author: Wu Jingwei
"""
"""
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()

arrr=[]
k=0
arr=range(3,100,2)
ar=[2]
ar+=arr
print ar
while len(ar)!=0:
    ar=filter(lambda x:x%n!=0,ar)
    k+=1
    print ar,k
print arrr
"""