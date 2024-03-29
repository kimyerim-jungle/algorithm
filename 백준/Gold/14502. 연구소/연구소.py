import sys, copy
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

area = []
for i in range(N):
    area.append(list(map(int, sys.stdin.readline().split())))
    

def bfs(a, b, area3, visited):
    queue = deque()
    queue.append([a,b])
 
    while queue:
        x, y = queue.popleft()
        if visited[x][y] == 1:
            continue
        
        visited[x][y] = 1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if area3[nx][ny] == 0:
                    area3[nx][ny] = 2
                    queue.append([nx, ny])
                    
   
def safe(area, com):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    area2 = copy.deepcopy(area)
    
    # 벽세우고
    for c in com:
        x = c[0]
        y = c[1]
        area2[x][y] = 1
    
    # 바이러스 퍼뜨리고 -> 2를 찾아서 bfs 시작 -> 0이면 2로 만들면서 어쩌구
    for i in range(N):
        for j in range(M):
            if area2[i][j] == 2 and visited[i][j] == 0:
                bfs(i, j, area2, visited)
    #for m in area2:
    #    print(m, end='\n')
    #print()
    # 안전구역 카운트
    count = 0
    for i in range(N):
        for j in range(M):
            if area2[i][j] == 0:
                count += 1
    return count


wall = []
for i in range(N):
    for j in range(M):
        if area[i][j] == 0:
            wall.append([i, j])
            
wall = list(combinations(wall, 3))

count = []
c = 0
for com in wall:
    count.append(safe(area, com))
    
print(max(count))