N = int(input())

nums = [0 for _ in range(10)]

while N >= 10:
    r = N % 10
    N = int(N / 10)
    nums[r] += 1
nums[N] += 1

if nums[6] >= 2 or nums[9] >= 2:
    if (nums[6] + nums[9]) % 2 == 1:
        a = int((nums[6] + nums[9]) / 2) + 1
    else: 
        a = int((nums[6] + nums[9]) / 2)
    nums[6] = a
    nums[9] = a 
print(max(nums))