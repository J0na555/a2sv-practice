n , s = input().split()
arr = list(map(int, input().split()))

arr.sort()
sum = 0
for i in range(len(arr)):
    idx = i
    if sum < s: 
        sum += arr[i]
        break

print(idx)
