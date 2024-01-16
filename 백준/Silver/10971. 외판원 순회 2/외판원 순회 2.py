import sys

num = int(input())

city = []
for i in range(num):
    city.append(list(map(int, sys.stdin.readline().split())))
'''    
도시 0~n-1 까지
city[][] = 0이면 pass
결과[] 만들어서 .append(sum += city[][])
비용 저장할때 [i][j]ㅇㅔ 대한 bool 리스트 필요
방문할 때 true 로 바꿔주고
한 바퀴 돌면 false로 초기화
sum끼리 비교해서 최소 출력
루트까지 저장할 필요 ㄴㄴ

마지막 도시에서는 첫 도시로 돌아가야해
'''
def TSP(N): # 시작 도시 번호 0 ~ N-1
    city_flag = [False] * N
    result = [] # 총 비용을 저장할 리스트
    start_city = 0
    
    def go(start, arr, count, cost): # 출발, 도착하는 도시, 몇 번째 방문인지, 그 동안의 비용
        cost += city[start][arr]
        #print(f'start : {start} arr : {arr} count : {count} cost = {cost}')
        
        if count >= N - 1: # 마지막 방문이면
            if city[arr][start_city] == 0:
                return
            else:
                cost += city[arr][start_city] # 돌아가는 비용 계산
                result.append(cost)
                #print(cost)
            return
        else: # 더 가야하면
            for i in range(N):
                if not city_flag[i]: # 아직 방문하지X
                    if city[arr][i] > 0: # 길이 존재
                        city_flag[i] = True
                        go(arr, i, count+1, cost)
                        city_flag[i] = False     
                             
    
    for i in range(N):
        city_flag[i] = True
        start_city = i
        for j in range(N):
            if not city_flag[j]:
                if city[i][j] != 0: # 길이 있는 도시면
                    city_flag[j] = True
                    go(i, j, 1, 0)
                    city_flag[j] = False
        city_flag[i] = False
                
    #print(result)
    return min(result)

print(TSP(num))