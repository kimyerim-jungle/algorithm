import sys
from collections import deque
#import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
degree = [0] * (N+1)
for _ in range(M): # i가 j 앞에 서야함 i가 출력되어야 j가 나올 수 있음
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    degree[j] += 1

q = deque()
for i in range(1, len(degree)):
    if degree[i] == 0: # 진입차수 없는거 push
        q.append(i)

result = []
while q:
    n = q.popleft()  
    result.append(n)
    for i in graph[n]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)
            
for i in result:
    print(i, end=' ')