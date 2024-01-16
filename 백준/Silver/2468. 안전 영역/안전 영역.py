import sys
sys.setrecursionlimit(100000)

num = int(input())

area = []
min_area = []
max_area = []
for i in range(num):
    area.append(list(map(int, sys.stdin.readline().split())))
    min_area.append(min(area[i]))
    max_area.append(max(area[i]))
    
safe_min = min(min_area)
safe_max = max(max_area)
'''
안전 영역의 최대 개수
높이 1이면 다 안 잠기니까 영역 1개

min부터 max-1까지 반복

안전지역 확정 = True

한 번 반복할때마다 flag 초기화하고
안전지역 .append

상하좌우 연결되면 한 개
가능한 조건이면 스택에 넣어
상하좌우 검색 가능한거 스택에 넣고 변수++
스택에 넣을ㄸㅐ count++
안 되는거 만나면 poppoppop
'''

safe = [] # 안전지역 개수 리스트
list = []
def safe_(N): # N = 높이 N이하는 잠긴다
    area_flag = []
    for i in range(num):
        area_flag.append([False] * num)
    count = 0
    
    def search(i, j, count):
        #print(f'area[{i}][{j}] | count = {count}')
        # 침수되지 않으면서 방문한 적 없는 지역
        
        if i - 1 >= 0:
            if area[i - 1][j] > N and not area_flag[i - 1][j]: # 상
                area_flag[i - 1][j] = True
                #print(f's1: {area_flag[i-1][j]}, {i-1}, {j}')
                count += 1
                count = search(i - 1, j, count)
        if j - 1 >= 0:    
            if area[i][j - 1] > N and not area_flag[i][j - 1]: # 좌
                area_flag[i][j - 1] = True
                #print(f's2: {area_flag[i][j-1]}, {i}, {j-1}')
                count += 1
                count = search(i, j - 1, count)
        if j + 1 < num:  
            if area[i][j + 1] > N and not area_flag[i][j + 1]: # 우
                area_flag[i][j + 1] = True
                #print(f's3: {area_flag[i][j + 1]}, {i}, {j + 1}')
                count += 1
                count = search(i, j + 1, count)
        if i + 1 < num: 
            if area[i + 1][j] > N and not area_flag[i + 1][j]: # 하
                area_flag[i + 1][j] = True
                #print(f's4: {area_flag[i + 1][j]}, {i + 1}, {j}')
                count += 1
                count = search(i + 1, j, count)
        return count
    
    for i in range(num):        
        for j in range(num):
            if area[i][j] <= N:
                #print(f'continue: {i}, {j}')
                continue
            
            elif not area_flag[i][j]: # N보다 크면서 방문하지 않은 지역
                #print(f'meet: {area_flag[i][j]}, {i}, {j}')
                count += 1
                area_flag[i][j] = True
                count = search(i, j, count)
                # 순회가 끝나면
                #print(f'count: {count}')
                list.append(count)
                count = 0
            #else:
                #print(f'else: {area_flag[i][j]}, {i}, {j}')
                
    
for i in range(0, safe_max):
    safe_(i)
    safe.append(list)
    list = [] # 초기화

if safe:
    #print(safe)
    safe_len = []
    for s in safe:
        safe_len.append(len(s))
    print(max(safe_len))
else:
    print(0)