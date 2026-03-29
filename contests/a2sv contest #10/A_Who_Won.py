t = int(input())

for _ in range(t):
    x0, y0 = list(map(int, input().split()))
    x1, y1 = list(map(int, input().split()))

    first_leader = (x0 > y0) #true if team 1 leads otherwise false
    last_leader = (x1 > y1)  # true if team 1 wins otherwise false



    if first_leader == last_leader:
        print("YES")
    else:
        print("NO")
