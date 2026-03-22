# import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # a.sort()
    i = j = 0
    op = 0

    while i < n and j < n:
        if a[i] <= b[j]:
            i += 1
            j += 1
        else:
            op += 1
            j += 1
    


    # for i in range(n-1):
    #     gap = a[i+1] -a[-1]
    #     if gap > 200:
    #         op += math.ceil(gap/200) + 1

    print(op)