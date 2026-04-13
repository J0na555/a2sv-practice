group_of_people, bus_capacity = list(map(int, input().split()))
groups = list(map(int, input().split()))


bus = 1
cur = 0
for people in groups:
    if cur + people <= bus_capacity:
        cur += people
    else:
        bus += 1
        cur = people

print(bus)



