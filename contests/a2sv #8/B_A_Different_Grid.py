t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    arr  = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    # only one cell
    if n*m == 1:
        print(-1)
        continue
    
    copy_arr = [[0] * m for _ in range(n)]

    first = arr[0][0]


  
    for i in range(n):
        for j in range(m):
            # shift the first to the back
            if i == 0 and j == 0:
                copy_arr[n-1][m-1] = first
            else:
                # current gets the prev elements value
                if j == 0:
                    copy_arr[i][j] = arr[i-1][m-1]
                else:
                    copy_arr[i][j] = arr[i][j-1]
    
    for row in copy_arr:
        print(' '.join(map(str, row)))