n, m = list(map(int, input().split())) 

student_answers = []
for _ in range(n):
    student_answers.append(input().strip())

marks = list(map(int, input().split()))

total = 0

for j in range(m):
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    
    for i in range(n):
        answer_given = student_answers[i][j]
        counts[answer_given] += 1
    
    max_freq = max(counts.values())
    
    total += max_freq * marks[j]

print(total)

# time  = o(nxm)
# space = o(nxm)


# A B C
# A A A
# B A C

# the first loop gets the first answer of the whole students  

