n = int(input())
time = list(map(int, input().split()))

rest = 0
max_rest = 0

times = time + time 

for hour in times:
    if hour == 1:
        rest += 1

        if rest > n:
            rest = n

        max_rest = max(max_rest, rest)

    else:
        rest = 0


print(max_rest)
