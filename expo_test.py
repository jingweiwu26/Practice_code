import timeit


def andrew_pow(X, n):
    memo={}
    if n == 0: memo[(X,n)] = 1
    elif n%2 == 1: memo[(X,n)] = andrew_pow(X, n-1) * X
    else: t = andrew_pow(X, n//2); memo[(X,n)]=t*t
    return memo[X,n]


def man_made(X, n):
    aa = 1
    while n > 1:
        aa *= X
        n -= 1
    return aa


def built_in(X, n):
    return pow(X, n)

if __name__ == '__main__':
    num = 1000
    print('man_made: {}'.format(timeit.repeat("for n in range(1000): man_made(2, n)", "from __main__ import man_made",
                                              number=num)))
    print('andrew_pow: {}'.format(timeit.repeat("for n in range(1000): andrew_pow(2, n)", "from __main__ import andrew_pow",
                                              number=num)))
    print('Built_in: {}'.format(timeit.repeat("for n in range(1000): built_in(2, n)", "from __main__ import built_in",
                                              number=num)))