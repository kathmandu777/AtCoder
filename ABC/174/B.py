n, d = map(int, input().split())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

ans = 0
for l in li:
    if (l[0] * l[0] + l[1] * l[1] <= d * d):
        ans += 1

print(ans)
