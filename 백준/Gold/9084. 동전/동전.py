import sys

num = int(input())

for _ in range(num):
    coin = []
    result = [0 for _ in range(10001)]
    result[0] = 1
    C = int(sys.stdin.readline().strip())
    coin.extend(list(map(int, sys.stdin.readline().split())))
    goal = int(sys.stdin.readline().strip())
    for i in range(len(coin)):
        for j in range(coin[i], goal+1):
            result[j] += result[j - coin[i]]

    print(result[goal])