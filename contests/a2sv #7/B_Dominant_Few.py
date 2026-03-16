# skill(elite) > skill(crowd)
# count(elite) < count(crowd)



# t = int(input())

# for _ in range(t):
#     n = int(input())
#     skill = list(map(int, input().split()))

#     skill.sort(reverse=True)
#     possible = False

#     for k in range(1, n):
#         elite = sum(skill[:k])
#         crowd = sum(skill[k:])

#         if k < n - k and elite > crowd:
#             possible = True
#             break

#     print("YES" if possible else "NO")


# -------------------------------------------------------------------

t = int(input())

for _ in range(t):
    n = int(input())
    arr = sorted(map(int, input().split()))
    
    prefix = [0]*(n+1)
    
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    
    possible = False
    
    for elite in range(1, n):
        crowd = elite + 1
        
        if elite + crowd > n:
            break
        
        elite_sum = prefix[n] - prefix[n-elite]
        crowd_sum = prefix[crowd]
        
        if elite_sum > crowd_sum:
            possible = True
            break
    
    print("YES" if possible else "NO")


    # 0(nlogn)
    # 0(n)