n, k = list(map(int, input().split()))

nums = list(map(int, input().split()))
nums.sort()


if nums[k-1] == nums[k]:
    print(-1)
else:
    print(nums[k-1]+1)