import sys
import heapq
import math

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j, w = map(int, sys.stdin.readline().split())
    graph[i].append((w, j))
    
A, B = map(int, sys.stdin.readline().split())

sum = 0
distance = [math.inf] * (N+1)

def dstra(graph, start, arr):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        w, now = heapq.heappop(q)
        
        if distance[now] < w:
            continue
        
        for i in graph[now]:
            if distance[i[1]] > i[0] + distance[now]:
                distance[i[1]] = i[0] + distance[now]
                heapq.heappush(q, (distance[i[1]], i[1]))                
                
    return distance[arr]
         
sum = dstra(graph, A, B)
print(sum)