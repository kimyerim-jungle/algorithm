N = int(input())


def is_prime(num):
    
    if num % 2 == 0:
        print(2)
        return int(num/2)
    if num % 3 == 0:
        print(3)
        return int(num/3)
    
    for i in range(5, num+1, 2):
        if num % i == 0:
            print(i)
            return int(num/i)
            
    
if N > 1:
    while N != 1:
        N = is_prime(N)
      
   
