import sys
 
v, e = map(int, sys.stdin.readline().split())
edges = [] * e
for i in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    edges.append((w, a, b))
    
parent = [0] * (v+1)
for i in range(len(parent)):
    parent[i] = i

edges.sort()

def kruskal(parent):
    result = 0
    
    def find(parent, x): # x노드의 부모 노드 찾기
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        
        if a < b :
            parent[b] = a
        else:
            parent[a] = b
        
    for edge in edges:
        if find(parent, edge[1]) == find(parent, edge[2]):
            continue
        else:
            union(parent, edge[1], edge[2])
            result += edge[0]
    return result

print(kruskal(parent))