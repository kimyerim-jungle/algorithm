import sys

nums = list(map(int, sys.stdin.readline().split()))

N = nums[0]
K = nums[1]

list = []
for i in range(N):
    list.append(i + 1)
    
answer = [] # pop된 사람들을 순서대로 입력
index = 0
while len(list) > 0:
    index += K
    index -= 1
    while index >= len(list):
        index = index - len(list) 
    
    answer.append(list[index])
    del list[index]

print("<", end="")
for i in range(len(answer)):
    if i == len(answer) - 1:
        print(answer[i], end="")
        break
    print(answer[i], end=", ")
print(">")