import itertools

n, m, q = map(int, input().split())
li = []
for i in range(q):
    li.append(list(map(int, input().split())))

Alist = list(itertools.combinations_with_replacement(range(1, m + 1), n))

answer = []
for i in range(len(Alist)):
    score = 0
    for j in range(q):
        b = li[j][1]-1
        a = li[j][0]-1
        if (Alist[i][b] - Alist[i][a] == li[j][2]):
            score += li[j][3]
    answer.append(score)

print(max(answer))
