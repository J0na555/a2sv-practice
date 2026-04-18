t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    min_char = min(s)
    pos = -1
    res = s

    for i in range(n-1, -1, -1):
        if s[i] == min_char:
            pos = i
            break

    
    char_to_move = s[pos]
    before = s[:pos]
    after = s[pos + 1:]
    
    res = char_to_move + before + after 
    

        # if s[i] > min_char:
        #     char_to_move = s[pos]
        #     before = s[:i]
        #     middle = s[i:pos]
        #     after = s[pos+1:]
        #
        #     res =  char_to_move + before + middle + after
        #     break
        #
        #
        # if s[i] < min_char:
        #     min_char = s[i]
        #     pos = i


    print(res)
