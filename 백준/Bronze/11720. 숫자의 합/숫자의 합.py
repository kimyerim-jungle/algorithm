T = int(input())
N = input().strip()

nums = [0 for _ in range(10)]

for i in range(len(N)):
    x = int(N[i])
    nums[x] += 1

count = 0
for i in range(10):
    count += i * nums[i]

print(count)   
