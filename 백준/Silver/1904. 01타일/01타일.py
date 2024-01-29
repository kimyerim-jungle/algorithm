num = int(input())

save = [0 for _ in range(15747)]

a, b = 1, 1

for _ in range(1, num + 1):
    a, b = b, (a+b)%15746
print(a)