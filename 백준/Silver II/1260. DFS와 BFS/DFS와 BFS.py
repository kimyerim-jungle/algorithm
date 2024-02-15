import sys
from collections import deque
import heapq

v, e, start = map(int, sys.stdin.readline().split())
graph = []
for i in range(v+1):
    graph.append([])
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def search(graph, start):
    
    def dfs(start, visited):
        stack = []
        stack.append(start)
        
        while stack:
            visit = stack.pop()
            
            if not visited[visit]:
                visited[visit] = True
                print(visit, end=' ')
                for edge in graph[visit]:
                    if not visited[edge]:
                        stack.append(edge)
                        #print(f'append: {edge}')
            
    def bfs(start, visited):   
        queue = deque()
        
        queue.append(start)
        
        while queue:
            visit = queue.popleft()
            
            if not visited[visit]:
                print(visit, end=' ')
                visited[visit] = True
                for edge in graph[visit]:
                    queue.append(edge)
        
    for i in range(1, v+1):
        graph[i] = sorted(graph[i], reverse=True)
    visited = [False] * (v+1)
    dfs(start, visited)
    print()
    
    for i in range(1, v+1):
        graph[i] = sorted(graph[i], reverse=False)
    visited = [False] * (v+1)
    bfs(start, visited)
    
search(graph, start)