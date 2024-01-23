import sys
sys.setrecursionlimit(100010)

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1): # i가 j 앞에 서야함 i가 출력되어야 j가 나올 수 있음
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
 
parent = [-1] * (N+1)   
def dfs(n):
    if visited[n]:
        return
    else:
        visited[n] = True
        for i in graph[n]:
            #print(f'graph[{n}]: {i}')
            if not visited[i]:
                parent[i] = n
                dfs(i)
                
dfs(1)

for i in range(2, len(parent)):
    print(parent[i])