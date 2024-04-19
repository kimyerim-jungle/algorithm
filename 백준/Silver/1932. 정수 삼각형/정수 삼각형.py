import sys

N = int(input())
      
nums = []
answer = []

for i in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))
    answer.append([-1 for j in range(i+1)])

answer[0][0] = nums[0][0]    
for i in range(N-1):
    for j in range(i+1):
        if answer[i+1][j] < answer[i][j] + nums[i+1][j]:
            answer[i+1][j] = answer[i][j] + nums[i+1][j]
        if answer[i+1][j+1] < answer[i][j] + nums[i+1][j+1]:
            answer[i+1][j+1] = answer[i][j] + nums[i+1][j+1]
            
print(max(answer[N-1]))
