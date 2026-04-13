t = int(input())


for _ in range(t):   
    n, k = list(map(int, input().split()))
    s = list(input().strip())

    countB = s.count('B')

    if countB == k:
        print(0)

    elif countB > k:
        need_to_remove = countB - k
        cnt = 0

        for i in range(n):
            if s[i] == 'B':
                cnt += 1

                if cnt == need_to_remove:
                    print(1)
                    print(i + 1, 'A')
                    break
    else:
        need_to_add = k - countB
        cnt = 0

        for i in range(n):
            if s[i] == 'A':
                cnt += 1
                
                if cnt == need_to_add:
                    print(1)
                    print(i + 1, 'B')
                    break
    


