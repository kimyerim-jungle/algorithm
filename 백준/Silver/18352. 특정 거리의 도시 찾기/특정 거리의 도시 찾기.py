import sys
from collections import deque

N, M, K, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)

def bfs(start):
    queue = deque()
    queue.append(start)
    length = [1000009] * (N + 1)
    length[start] = 0 
    while queue:
        node = queue.popleft()
        if visited[node]:
            continue
        else:
            visited[node] = True
            for edge in graph[node]:
                if not visited[edge]:
                    queue.append(edge)
                    if length[edge] <= length[node] + 1:
                        pass
                    else:
                        length[edge] = length[node] + 1
    return length        
            
length = bfs(start)
result = [] 
for i in range(len(length)):
    if length[i] == K:
        result.append(i)
        
if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)
        
        
    