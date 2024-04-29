def sov(num):
    number = []
    tmp = num
    while num >= 10:
        number.append(num % 10)
        num = int(num / 10)
    number.append(num)
    return tmp + sum(number)
    

s = int(input())
ans = 0
tmp = s
answer = []

while tmp >= s/2:
    tmp = tmp - 1
    ans = sov(tmp)
    if ans == s:
        answer.append(tmp)

if len(answer) == 0:
    print(0)
else:   
    print(min(answer))