def main(input=0):
    coins = [1, 3, 5]
    lis = [i for i in range(input+1)] # [0,1]
    for i in range(1, input+1):
        for coin in coins:
            if i - coin >= 0 and lis[i-coin] + 1 < lis[i]:
                lis[i] = lis[i-coin] + 1
    return lis[-1]


if __name__ == '__main__':
    print(main())