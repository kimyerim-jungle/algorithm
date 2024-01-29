num = int(input())

a, b = 1, 1

for _ in range(1, num + 1):
    a, b = b, (a+b)%15746
print(a)