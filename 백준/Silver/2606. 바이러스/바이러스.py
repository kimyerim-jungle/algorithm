import sys

v = int(input())
e = int(input())
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
        if visited[node]:
            continue
        else:
            visited[node] = True
            count += 1
        
        for edge in edges[node]:
            if not visited[edge]:
                stack.append(edge)
                    
    return count - 1 # 1번 컴퓨터는 빼줌
        
    
count = dfs(1, count)
        
print(count)