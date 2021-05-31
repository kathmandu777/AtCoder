import sys
import itertools

n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

for i in itertools.combinations(li, 3):
    if (0.5 * abs((i[0][0] - i[2][0]) * (i[1][1] - i[2][1]) - (i[1][0] - i[2][0]) * (i[0][1] - i[2][1]))) == 0:
        print("Yes")
        sys.exit()
print("No")
