n = int(input())
color = str(input().strip())


if n == 1:
    print("Yes")
elif len(set(color)) == n:
    print("No")
else:
    print("Yes")