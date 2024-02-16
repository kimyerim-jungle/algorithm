import sys 

N = int(input())
score = list(map(int, sys.stdin.readline().split()))
big = max(score)
sum = 0

for i in range(len(score)):
    score[i] = score[i]/big*100
    sum += score[i]
print(sum/len(score))