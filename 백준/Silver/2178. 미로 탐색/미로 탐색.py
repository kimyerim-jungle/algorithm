import sys
from collections import deque

row, col = map(int, input().split())
graph = [[] for _ in range(row)]
visited = [[False] * col for _ in range(row)]

for i in range(row):
    string = sys.stdin.readline().strip()
    for j in range(col):
        graph[i].append(int(string[j]))
#print(graph)
count = 0
# 범위 0~N-1, M-1
def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))  # x, y 튜플로 관리
    
    #(N, M)에 도착할때까지...
    while queue:
        cur_x, cur_y = queue.popleft()
        if cur_x == row-1 and cur_y == col-1:
            break
        
        if visited[cur_x][cur_y]:
            continue
        else:
            visited[cur_x][cur_y] = True
            # 돌면서 방문 안 한 값이 1인 좌표로 이동
            # 1값부터 시작해서 무조건 사방 중 하나에 1이 있음 1을 찾아서 넣으면 댐
            if cur_y+1 < col and not visited[cur_x][cur_y+1] and graph[cur_x][cur_y+1]: # 우
                queue.append((cur_x, cur_y+1))
                graph[cur_x][cur_y+1] = graph[cur_x][cur_y] + 1
            if cur_x+1 < row and not visited[cur_x+1][cur_y] and graph[cur_x+1][cur_y]: # 하
                queue.append((cur_x+1, cur_y))
                graph[cur_x+1][cur_y] = graph[cur_x][cur_y] + 1
            if cur_y-1 >= 0 and not visited[cur_x][cur_y-1] and graph[cur_x][cur_y-1]: # 좌
                queue.append((cur_x, cur_y-1))
                graph[cur_x][cur_y-1] = graph[cur_x][cur_y] + 1
            if cur_x-1 >= 0 and not visited[cur_x-1][cur_y] and graph[cur_x-1][cur_y]: # 상
                queue.append((cur_x-1, cur_y))
                graph[cur_x-1][cur_y]  = graph[cur_x][cur_y] + 1
            
bfs(0, 0)
        
print(graph[row-1][col-1])