import sys

N = int(input())
change = {}
num = list(map(int, sys.stdin.readline().split()))

sorting = list(set(num))
sorting.sort()

for i in range(len(sorting)):
    if sorting[i] in change.keys():
        continue
    change[sorting[i]] = i

for i in num:
    print(change[i], end=" ")