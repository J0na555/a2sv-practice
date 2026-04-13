n = int(input())
problems = list(map(int, input().split()))

problems.sort()
# problem_set = set(problems)
#
# print(len(problem_set))

day = 1

for problem in problems:
    if problem >= day:
        day += 1

print(day - 1)

# on day k, he must solve exactly k problems from a contest that has at least k problems.
