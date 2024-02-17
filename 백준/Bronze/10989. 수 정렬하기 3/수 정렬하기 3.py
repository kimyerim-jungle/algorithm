import sys

N = int(input())
number = [0 for _ in range(10001)]
for _ in range(N):
    a = int(sys.stdin.readline().strip())
    number[a] += 1

for i in range(len(number)):
    for j in range(number[i]):
        print(i)