max = 0

for i in range(9):
    num = int(input())
    if(num > max):
        max = num
        count = i + 1
        
print(max)
print(count)