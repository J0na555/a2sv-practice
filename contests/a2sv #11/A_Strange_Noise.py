t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip().lower()

    cat = s[0]

    for i in range(1, n):
        if s[i] != s[i-1]:
            cat += s[i]

    print("YES" if cat == 'meow' else "NO")
