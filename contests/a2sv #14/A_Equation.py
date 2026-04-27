def is_composite(n):
    if n <= 3:
        return False
    
    if n % 2 == 0:
        return True
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return True
        i += 2
        
    return False

n = int(input())
a = (n // 4 + 1) * 4

while True:
    b = a - n

    if is_composite(b):
        print(f"{a} {b}")
        break         
    a += 4

# 512 = 4608 - 4096
# 5608 = 4096 + 512
# i only need to get one composite number 
# after getting one just substract n from it and check if that number is composite as well
# if not try another composite number


