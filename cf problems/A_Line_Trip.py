t = int(input())

for _ in range(t):
    n, x = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    ans = nums[0] - 0
    
    for i in range(1, n):
        gap = nums[i] - nums[i-1]
        if gap > ans:
            ans = gap
            
    last_gap = 2 * (x - nums[-1])
    if last_gap > ans:
        ans = last_gap
        
    print(ans)
