import sys
from collections import deque

col, row, height = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(row)] for _ in range(height)]

grow = [[0, -1, 0], [1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]]  # 좌상우하 x,y,z

def bfs():
    
    while q:
        z, x, y = q.popleft()
        
        for i in range(6):
            nz = z + grow[i][2]
            nx = x + grow[i][0]
            ny = y + grow[i][1]
            if 0 <= nz < height and 0 <= nx < row and 0 <= ny < col:
                if graph[nz][nx][ny] == 0 :
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    q.append((nz, nx, ny))
                           
q = deque()   
for h in range(height):
    for r in range(row):
        for c in range(col):
            if graph[h][r][c] == 1:
                q.append((h,r,c))
bfs()

success = True
day = -1
for h in range(height):
    for r in range(row):
        for c in range(col):
            if graph[h][r][c] == 0:
                success = False
            day = max(day, graph[h][r][c])
        
if success:
    print(day-1)
else:
    print(-1)