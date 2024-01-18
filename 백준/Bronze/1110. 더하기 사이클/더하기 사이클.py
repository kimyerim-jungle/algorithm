num = int(input())

sum = 0

a = num // 10
b = num % 10
sum = a + b
n = b*10 + sum%10
count = 1

while n != num:
    a = n // 10
    b = n % 10
    
    sum = a + b
    n = b*10 + sum%10
    #print(a, b)
    count += 1

print(count) 