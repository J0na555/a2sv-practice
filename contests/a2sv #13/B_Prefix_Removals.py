t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    res = ""
    
    min_char = min(s)
    
    for i in range(len(s)-1, 0, -1):
        if s[i] == min_char:
            res = s[i] + s[:i] + s[i+1:]
            break
    
    if res == "":
        res = s
    print(res)
