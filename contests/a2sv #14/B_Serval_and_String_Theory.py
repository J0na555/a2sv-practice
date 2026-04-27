t = int(input())

for _ in range(t):
    len_s, operations = list(map(int, input().split()))
    s = input()

    if len_s == 1:
        print("NO")
        continue

    if s < s[::-1]:
        print("YES")
        continue

    if operations == 0:
        print("NO")
        continue

    if len(set(s)) == 1:
        print("NO")
        continue

    print("YES") 







# imposible len = 1
# already universal
# not universal but no operations
# same characters
# otherwise yes
