t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    dust = nums[:-1]
    total_dust = sum(dust)
    
    start = 0
    while start < len(dust) and dust[start] == 0:
        start += 1
    
    zeros_after = 0

    for i in range(start, len(dust)):
        if dust[i] == 0:
            zeros_after += 1
    
    res = total_dust + zeros_after

    print(res)



    


