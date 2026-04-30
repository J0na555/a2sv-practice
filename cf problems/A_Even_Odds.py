n, k = list(map(int, input().split()))

mid = (n + 1) // 2

if k <= mid:
    print(2 * k - 1)

else:
    print(2 * (k - mid))
