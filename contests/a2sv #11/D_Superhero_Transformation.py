s = input().strip().lower()
t = input().strip().lower()

if len(s) != len(t):
    print("NO")

else:

    vowels = set('aeiou')
    hero = True

    for i in range(len(s)):
        s_is_hero = s[i] in vowels
        t_is_hero = t[i] in vowels
        
        if s_is_hero != t_is_hero:
            hero = False
            break

    print("Yes" if hero else "No")


    # time complexity = 0(n)
    # space complexity = 0(1)
