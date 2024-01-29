import sys

N, K = map(int, input().split())
list = []
for _ in range(N):
    list.append(int(sys.stdin.readline().strip()))

count = 0
i = N-1
while i >= 0:
    if K < list[i]:
        i -= 1
    elif K >= list[i]:
        num = K // list[i]
        count = count + num
        K = K - list[i] * num
        
    if K <= 0:
        break

print(count)