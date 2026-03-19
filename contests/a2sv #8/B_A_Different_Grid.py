# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())

#     arr  = []
#     for _ in range(n):
#         arr.append(list(map(int, input().split())))

#     # only one cell
#     if n*m == 1:
#         print(-1)
#         continue
    
#     copy_arr = [[0] * m for _ in range(n)]

#     first = arr[0][0]


  
#     for i in range(n):
#         for j in range(m):
#             # shift the first to the back
#             if i == 0 and j == 0:
#                 copy_arr[n-1][m-1] = first
#             else:
#                 # current gets the prev elements value
#                 if j == 0:
#                     copy_arr[i][j] = arr[i-1][m-1]
#                 else:
#                     copy_arr[i][j] = arr[i][j-1]
    
#     for row in copy_arr:
#         print(' '.join(map(str, row)))























# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())

#     arr = []
#     for _ in range(n):
#         arr.append(list(map(int, input().split())))

#     if n * m == 1:
#         print(-1)
#         continue

#     # flatten
#     flat = []
#     for row in arr:
#         flat.extend(row)

#     # rotate
#     flat = flat[1:] + flat[:1]

#     # rebuild grid
#     idx = 0
#     for i in range(n):
#         row = flat[idx:idx+m]
#         idx += m
#         print(*row)
  



# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     a = [list(map(int, input().split())) for _ in range(n)]

#     if n == 1 and m == 1:
#         print(-1)
#         continue

#     if m > 1:
#         for i in range(n):
#             row = a[i][1:] + [a[i][0]]
#             print(*row)
#     else:
#         for i in range(n):
#             print(a[(i+1) % n][0])





t = int(input())
    
for _ in range(t):
    n, m = map(int, input().split())
    
    # Read the board
    board = []
    for _ in range(n):
        row = list(map(int, input().split()))
        board.append(row)
    
    # Check if it's impossible
    if n == 1 and m == 1:
        print(-1)
        continue
    
    # Flatten the board
    flat = []
    for i in range(n):
        for j in range(m):
            flat.append(board[i][j])
    
    # Perform cyclic shift to the left
    shifted = flat[1:] + [flat[0]]
    
    # Reshape back to n x m
    result = []
    idx = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(shifted[idx])
            idx += 1
        result.append(row)
    
    # Output the result
    for row in result:
        print(' '.join(map(str, row)))

