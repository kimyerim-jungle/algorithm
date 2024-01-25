import sys

N = int(input()) # 가로세로N

graph = [[] for _ in range(N)]

for i in range(N):
    string = sys.stdin.readline().strip()
    for j in range(N):
        graph[i].append(string[j])

visited = [[False for _ in range(N)] for _ in range(N)]
mov = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 좌상우하
def dfs(start_x, start_y, sum):
    
    if not visited[start_x][start_y]:
        visited[start_x][start_y] = True
        #print(f'visit| x={start_x},y={start_y}')
        for i in range(4):
            next_x = start_x+mov[i][0]
            next_y = start_y+mov[i][1]
            
            if 0 > next_x or next_x >= N or 0 > next_y or next_y >= N:
                continue
            if not visited[next_x][next_y]:
                if graph[next_x][next_y] == '1': 
                    sum += 1
                    sum = dfs(next_x, next_y, sum)            
    return sum

sum = 1    
result = []             
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == '1':
            result.append(dfs(i, j, sum))
result.sort()            
print(len(result))
for i in range(len(result)):
      print(result[i])