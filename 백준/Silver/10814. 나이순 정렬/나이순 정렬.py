import sys
import heapq

N = int(input())

age = []
for i in range(N):
    num, name = sys.stdin.readline().split()
    heapq.heappush(age, (int(num), i, name))
    
for i in range(N):
    num, a, name = heapq.heappop(age)
    print(num, name)