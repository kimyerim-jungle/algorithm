import sys

N, M = map(int, sys.stdin.readline().split()) # 세로 N, 가로 M

graph = [[] for _ in range(N)]

for i in range(N):
    string = sys.stdin.readline().strip()
    for j in range(M):
        graph[i].append(string[j])

visited = [[False for _ in range(M)] for _ in range(N)]
mov = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 좌상우하
def dfs(start_x, start_y, sum):
    
    if not visited[start_x][start_y]:
        visited[start_x][start_y] = True
        #print(f'visit| x={start_x},y={start_y}')
        for i in range(4):
            next_x = start_x+mov[i][0]
            next_y = start_y+mov[i][1]
            
            if 0 > next_x or next_x >= N or 0 > next_y or next_y >= M:
                continue
            if not visited[next_x][next_y]:
                if graph[start_x][start_y] == '-': # 좌 우
                    if i % 2 == 0:
                        if graph[start_x][start_y] == graph[next_x][next_y]:
                            sum = dfs(next_x, next_y, sum)
                if graph[start_x][start_y] == '|': # 상 하
                    if i % 2 == 1:
                        if graph[start_x][start_y] == graph[next_x][next_y]:
                            sum = dfs(next_x, next_y, sum)
                        
    #print(sum)                 
    return sum

sum = 1    
result = 0             
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            result += dfs(i, j, sum)         
print(result)
    