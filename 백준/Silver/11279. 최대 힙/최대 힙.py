import heapq
import sys

heap = []

num = int(input())

for _ in range(num):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)
        