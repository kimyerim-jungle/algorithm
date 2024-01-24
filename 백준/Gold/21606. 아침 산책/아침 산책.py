import sys
sys.setrecursionlimit(2*10^5)

N = int(input())
graph = [[] for _ in range(N+1)]
string = sys.stdin.readline().strip()
in_out = [-1]
for i in range(len(string)):
    in_out.append(int(string[i]))
for _ in range(N-1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)


def bipartite(graph, count):
    
    def dfs(n, count, visited):  # 실내에서 시작, 실내를만나면 종료 모든 실내를 찾아서 실내 출발
        if visited[n]:
            return
        else:
            visited[n] = True
            for i in graph[n]:
                if not visited[i] and in_out[i] == 0: # 방문한 적 없는 실외
                    count = dfs(i, count, visited)
                if not visited[i] and in_out[i] == 1: # 방문한 적 없는 실내
                    visited[i] = True
                    count += 1                    
                
        return count
    
    
    for i in range(1, N+1):
        visited = [False] * (N+1)
        if not visited[i] and in_out[i] == 1:
            count = dfs(i, count, visited)
    return count
         
            
count = 0
count += bipartite(graph, count)
        
print(count)