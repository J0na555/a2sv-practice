t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    dust = nums[:-1]
    total_dust = sum(dust)

    cnt = 0

    for x in dust:
        if x > 0:
            cnt += 1

    if cnt > 0:
        res = total_dust + cnt - 1
    else:
        res = 0

    print(res)

    

