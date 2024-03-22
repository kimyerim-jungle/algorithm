import sys
from collections import deque

N = int(input())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def RGB_bfs(a, b, color, visited):
    queue = deque()
    queue.append([a, b])
    
    while queue:
        x, y = queue.popleft()
        
        if visited[x][y] == 1:
            continue
        
        visited[x][y] = 1
        c = color[x][y] # 무슨 색 탐색중인지
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if color[nx][ny] == c:
                    if visited[nx][ny] == 0:
                        queue.append([nx, ny])
    
    return 1
    

def RB_bfs(a, b, color, visited):
    queue = deque()
    queue.append([a, b])
    
    while queue:
        x, y = queue.popleft()
        
        if visited[x][y] == 1:
            continue
        
        visited[x][y] = 1
        c = color[x][y] # 무슨 색 탐색중인지
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if c == 'B':
                    if color[nx][ny] == 'B':
                        if visited[nx][ny] == 0:
                            queue.append([nx, ny])
                else:
                    if color[nx][ny] == 'R' or color[nx][ny] == 'G':
                        if visited[nx][ny] == 0:
                            queue.append([nx, ny])
    
    return 1
 
color = []   
for i in range(N):
    color.append(sys.stdin.readline().strip())

visited = [[0 for _ in range(N)] for _ in range(N)] 
RGB_count = 0 
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            RGB_count += RGB_bfs(i, j, color, visited)
            
visited = [[0 for _ in range(N)] for _ in range(N)]  
RB_count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            RB_count += RB_bfs(i, j, color, visited)
    
print(RGB_count, RB_count)    