import sys

num = list(map(int, sys.stdin.readline().split()))

M = num[0]
N = num[1]
L = num[2]
check = [False] * N

M_X = list(map(int, sys.stdin.readline().split())) # M의 X좌표값 리스트

animal = []
count = 0
for i in range(N):
    animal.append(sys.stdin.readline().split())

for i in range(len(M_X)): # 사대를 하나씩 순회
    for j in range(len(animal)): # 잡을 수 있는 동물이 있는지 검사
        if abs(M_X[i] - int(animal[j][0])) + int(animal[j][1]) <= L and not check[j]:
            count += 1
            check[j] = True
            
print(count)
