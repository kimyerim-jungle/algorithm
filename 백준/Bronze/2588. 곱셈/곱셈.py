A = int(input())
B = int(input())

b1 = B // 100
b2 = (B - b1*100) // 10
b3 = B - b1*100 - b2*10

print(A*b3)
print(A*b2)
print(A*b1)

print(A*B)