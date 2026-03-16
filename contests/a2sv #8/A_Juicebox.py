t = int(input())

for _ in range(t):
    shelves, boxes = list(map(int, input().split()))

    for _ in range(boxes):
        brand, cost = list(map(int, input().split()))

        