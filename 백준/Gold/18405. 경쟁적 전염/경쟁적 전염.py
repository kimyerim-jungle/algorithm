import sys
import heapq

N, K = map(int, sys.stdin.readline().split()) # 가로세로N, K번까지 바이러스
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

S, X, Y = map(int, sys.stdin.readline().split())

visited = [[0 for _ in range(N)] for _ in range(N)]
mov = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 좌상우하

q = [] 

def bfs(graph):
    
    while q:
        time, value, now_x, now_y = heapq.heappop(q)
        
        if time == S:
            return
        for i in range(4):
            next_x = now_x+mov[i][0]
            next_y = now_y+mov[i][1]
            
            if 0 > next_x or next_x >= N or 0 > next_y or next_y >= N:
                continue
            if graph[next_x][next_y] == 0:
                graph[next_x][next_y] = value
                heapq.heappush(q, (time+1, graph[next_x][next_y], next_x, next_y))


for i in range(N):
    for j in range(N):
        if graph[i][j] != 0: # 바이러스가 있는 경우
            heapq.heappush(q, (0, graph[i][j], i, j))
bfs(graph)
#print(graph)
print(graph[X-1][Y-1])