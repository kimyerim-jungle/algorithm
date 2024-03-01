import sys
from collections import deque

M, N = map(int, input().split())

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
def bfs(queue, t):
    while queue:
        x, y = queue.popleft()
        
        if t[x][y] == -1:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if t[nx][ny] == 0:
                    queue.append([nx, ny])
                    t[nx][ny] = t[x][y] + 1           
        

tomato = []
queue = deque()

for _ in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))

zero = -1
for i in range(N):
    if 0 in tomato[i]:
        zero = 0
if zero == -1:
    print(0)
else:
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                queue.append([i, j])
    
    bfs(queue, tomato)
    for i in range(N):
        if 0 in tomato[i]:
            zero = 1
    if zero == 1:
        print(-1)
    else:
        count = 1
        for i in range(N):
            for j in range(M):
                if count < tomato[i][j]:
                    count = tomato[i][j]
        print(count-1)

