import math

n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))

x = 0
y = 1

ans = 0
for i in range(n):
    for j in range(n):
        d = math.sqrt((xy[i][x] - xy[j][x]) ** 2 + (xy[i][y] - xy[j][y]) ** 2)
        ans = max(ans, d)

print(ans)
