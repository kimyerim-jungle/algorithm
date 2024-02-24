import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
c = []
for _ in range(N):
    c.append(list(map(int, sys.stdin.readline().split())))

count = 0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
queue = deque()

def bfs(x, y, c):
    count = 0
    
    while(True):
        queue.append((x, y))
        while(queue):
            cur_x, cur_y = queue.popleft()
            
            if c[cur_x][cur_y] == 0:
                c[cur_x][cur_y] = 'A'
                for i in range(4):
                    di = cur_x + dx[i]
                    dj = cur_y + dy[i]
                    if 0 <= di  < N and 0 <= dj < M and c[di][dj] == 0:
                        queue.append((di, dj))
        
        for i in range(N):
            for j in range(M):
                if c[i][j] == 1:
                    air = 0
                    for k in range(4):
                        di = i + dx[k]
                        dj = j + dy[k]
                        if 0 <= di < N and 0 <= dj < M:
                            if c[di][dj] == 'A':
                                air += 1
                    if air > 1 :
                        c[i][j] = 0
                        
        for i in range(N):
            for j in range(M):
                if c[i][j] == 'A':
                    c[i][j] = 0
   
        count += 1         
        if sum(sum(row) for row in c) == 0:
            break          
    print(count)
 

bfs(0, 0, c) # 외부공기로 시작
