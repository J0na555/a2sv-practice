t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    #  has only one cell so return -1
    if n == 1 and m == 1:
        print(-1)
        continue

    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = grid[(i + 1) % n][(j + 1) % m]

    for row in result:
        print(' '.join(map(str, row)))

# time complexity = O(n × m)
# space complexity = O(n × m)