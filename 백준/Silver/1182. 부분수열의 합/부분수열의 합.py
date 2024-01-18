import sys

N, goal = map(int, sys.stdin.readline().split())

list = list(map(int, sys.stdin.readline().split()))

global count
count = 0
def f(index, sum): # 개수 카운트, 합 목표, 몇 번째에서 시작
    global count
    if index == N:
        if sum == goal:
            count+=1
            return
        else:
            return
    
    #print(list[index], sum)
    f(index+1, sum)
    f(index+1, sum+list[index])
    
f(0, 0)

if goal == 0:
    count -= 1
print(count)