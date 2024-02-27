import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y, c, N, M):
    queue = deque()
    queue.append([x, y])
    
    while(queue):
        a, b = queue.popleft()
        
        if c[a][b] == 1:
            c[a][b] = 2
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < N and 0 <= ny < M and c[nx][ny] == 1:
                    queue.append([nx, ny])
    return 1

T = int(input())
for _ in range(T): 
    M, N, K = map(int, sys.stdin.readline().split())
    c = [[0 for _ in range(M)] for _ in range(N)]
    bae = deque()
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        c[b][a] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if c[i][j] == 1:
                count += bfs(i, j, c, N, M)
    
    print(count)      
