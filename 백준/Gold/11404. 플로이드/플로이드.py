import sys
import heapq
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)] 
result = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append((b, w))
    

for i in range(1, N+1):
    for j in graph[i]:
        if result[i][j[0]] < j[1]: continue
        result[i][j[0]] = j[1]
    result[i][i] = 0

for k in range(1, N+1):           
    for i in range(1, N+1):
        for j in range(1, N+1):
            if result[i][k] + result[k][j] < result[i][j]:
                result[i][j] = result[i][k] + result[k][j]
                
for i in range(1, N+1):
    for j in range(1, N+1):
        if result[i][j] == INF:
            result[i][j] = 0
        print(result[i][j], end=' ')
    print()
            