books, time = list(map(int, input().split()))
books_list = list(map(int, input().split()))

read = 0

for i in range(books):
    if books_list[i] < time: 
        read += 1

print(count)

