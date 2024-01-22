import sys

v, e = map(int, input().split())
edges = [[] for _ in range(v+1)]
visited = [False] * (v + 1)

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

stack = []
count = 0
def dfs(start, count):
    stack.append(start)
    
    while stack:
        node = stack.pop()
        visited[node] = True
        #print(f'pop={node}')
        
        for edge in edges[node]:
            if not visited[edge]:
                stack.append(edge)
                
    count += 1     
    return count
        
    
for i in range(1, v + 1):
    if not visited[i]:
        #print(f'count={count}')
        count = dfs(i, count)
        
print(count)