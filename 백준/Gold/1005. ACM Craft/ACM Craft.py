import sys
import heapq
import copy

T = int(input())

def ACM():
    N, K = map(int, input().split())

    time = list(map(int, sys.stdin.readline().split()))
    b = [[] for _ in range(N+1)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        b[y].append(x)
    win = int(input())
    spend = [0 for _ in range(N+1)]
    sp = [0 for _ in range(N+1)]
    build = []
    for i in range(1, N+1):
        heapq.heappush(build, [len(b[i]), time[i-1], i]) # 조건 개수, 건물 번호
    done = 0
    #print(build)
    while build:
        d = []
        
        while build:
            max_time = 0
            if build[0][0] != 0:
                break
            c, t, num = heapq.heappop(build)
            spend[num] += t
            for n in b[num]:
                if max_time < spend[n]:
                    max_time = spend[n]
            spend[num] += max_time
            d.append(num)
            
        for i in range(len(build)):
            j = build[i][2]
            for n in d:
                if n in b[j]:
                    build[i][0] -= 1
            if n == win:
                done = 1
                break  
        #print(spend)
        #spend += max_time
        if done == 1:
            break
        build.sort()
    
    max_time = 0
    for i in b[win]:
        if max_time < spend[i]:
            max_time = spend[i]
       
    return time[win-1] + max_time
  
        
for _ in range(T):
    print(ACM())
    #print(_)
