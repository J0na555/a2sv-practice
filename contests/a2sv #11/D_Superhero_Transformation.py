s = input().strip().lower()
t = input().strip().lower()

if len(s) != len(t):
    print("NO")

else:

    vowels = set('aeiou')
    hero = True
    s_is_hero = False
    t_is_hero = False

    for i in range(len(s)):
        if s[i] in vowels:
            s_is_hero = True
        if t[i] in vowels:
            t_is_hero = True
            
        if s_is_hero != t_is_hero:
            hero = False
            break

    print("Yes" if hero else "No")
