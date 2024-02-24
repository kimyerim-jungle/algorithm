N = int(input())

five = 0
a = 1
for i in range(1, N+1):
    a *= i
    if i % 5 == 0:
        while(i % 5 == 0):
            five += 1
            i /= 5
        
print(five)
