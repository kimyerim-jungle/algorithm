import sys
from collections import deque

N = int(input())


def dfs(stack, graph, visited):

    while stack:
        x, y = stack.pop()
        
        if visited[x][y] == 1 or graph[x][y] == 0: # 방문했거나 방문 불가능하면
            continue
        
        visited[x][y] = 1 # 방문체크

        for i in range(N):
            if graph[y][i] == 1:
                graph[x][i] = 1
                if visited[y][i] == 0:
                    stack.append([y, i])
                      
graph = []
stack = deque()
visited = [[0 for _ in range(N)]for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))  
    
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            stack.append([i,j])
            dfs(stack, graph, visited)

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()

