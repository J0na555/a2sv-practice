t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    l, r = 0, n-1
    # already palindrome
    if s == s[::-1]:
        print("Yes")
        continue

    # diff = []
    # for i in range(n//2):
    #     if s[i] != s[n - 1 - i]:
    #         diff.append(i)

    # one_chance = diff[-1] - diff[0] + 1

    # if diff and one_chance == len(diff):
    #     print("Yes")
    # else:
    #     print("No")

        # ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh what the fuck should i do now

    while l < r and s[l] == s[r]:
        l += 1
        r -= 1
    
    while l < r and s[l] != s[r]:
        l += 1
        r -= 1
    
    if l >= r:
        print("Yes")
    else:
        print("No")