list = input().split()

num = []

for i in list:
    num.append(int(i))


print(num[0]+num[1])
print(num[0]-num[1])
print(num[0]*num[1])
print(int(num[0]/num[1]))
print(num[0]%num[1])