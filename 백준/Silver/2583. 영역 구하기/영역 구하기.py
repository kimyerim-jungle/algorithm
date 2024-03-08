import sys
from collections import deque

M, N, K = map(int, input().split())

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
def bfs(queue, t):
    c = 0
    while queue:
        x, y = queue.popleft()
        
        if t[x][y] == 'v' or t[x][y] == -1:
            continue
        
        t[x][y] = 'v'
        c += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if t[nx][ny] == 0:
                    queue.append([nx, ny])
     
    return c              
        

nemo = [[0 for _ in range(N)] for _ in range(M)]
queue = deque()

for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for i in range(b, d):
        for j in range(a, c):
            nemo[i][j] += 1

count = []  
for i in range(M):
    for j in range(N):
        if nemo[i][j] == 0:
            queue.append([i,j])
            count.append(bfs(queue, nemo))

print(len(count))
count.sort()
for _ in count:
    print(_, end=' ')
