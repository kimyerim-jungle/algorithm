import sys
from collections import deque

dx = [0, 1, 0, -1, -1, -1, 1, 1] # 상하좌우 대각 좌상 우상 좌하 우하
dy = [-1, 0, 1, 0, -1, 1, -1, 1]

def bfs(x, y, s, W, H):
    queue = deque()
    queue.append([x, y])
    
    while(queue):
        a, b = queue.popleft()
        
        if s[a][b] == 1:
            s[a][b] = 2
            for i in range(8):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < H and 0 <= ny < W and s[nx][ny] == 1:
                    queue.append([nx, ny])
    return 1

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    s = []
    count = 0
    for _ in range(H):
        s.append(list(map(int, sys.stdin.readline().split())))
        
    for i in range(H):
        for j in range(W):
            if s[i][j] == 1:
                count += bfs(i, j, s, W, H)
    print(count)
 