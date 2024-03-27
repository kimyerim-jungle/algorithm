import sys
import heapq

N, E = map(int, input().split())
INF = 10**9
dijk = [[INF for _ in range(N+1)]for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    dijk[a][b] = c
    dijk[b][a] = c
    
v1, v2 = map(int, input().split())

d0 = [INF for _ in range(N+1)]
d1 = [INF for _ in range(N+1)] # v1 -> v2
d2 = [INF for _ in range(N+1)] # v2 -> N

#for i in range(2, N+1):
#    d0[i] = dijk[1][i]

d0[1] = 0    
d1[v1] = 0
d2[v2] = 0

def dijkstra (dist, start):
    queue = []
    heapq.heappush(queue, [0, start])
      
    while queue:
        w, v = heapq.heappop(queue)
        
        if w > dist[v]:
            continue
        
        for i in range(1, N+1):
            if dijk[v][i] == INF:
                continue
            else:
                new_dist = w + dijk[v][i]
                if dist[i] > new_dist:
                    dist[i] = new_dist
                    heapq.heappush(queue, [new_dist, i])

dijkstra(d0, 1)
dijkstra(d1, v1)
dijkstra(d2, v2)

last = min(d0[v1] + d1[v2] + d2[N], d0[v2] + d2[v1] + d1[N])
if last < INF:
    print(last)
else:
    print(-1)   

