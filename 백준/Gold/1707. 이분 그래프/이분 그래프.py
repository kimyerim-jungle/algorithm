import sys
sys.setrecursionlimit(200010)

def bipartite(graph, v):
    visited = [0] * (v+1) # <- color
    is_bipartite = True
    
    def dfs(n, color, is_bipartite):
        if visited[n] != 0:
            return
        
        visited[n] = color
        
        for i in graph[n]:
            #print(f'i={i}, v={visited[i]}, c = {color}')
            if visited[i] == color:
                is_bipartite = False
                break
            if visited[i] == 0:
                is_bipartite = dfs(i, -color, is_bipartite)
        return is_bipartite
                
    for i in range(1, v+1):
        if visited[i] == 0:
            is_bipartite = dfs(i, 1, is_bipartite)
            if is_bipartite == False:
                return 0
    return 1
                              
K = int(input())

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, sys.stdin.readline().split())
        graph[i].append(j)
        graph[j].append(i)
        
    if bipartite(graph, V) == 1:
        print('YES')
    else:
        print('NO')
    