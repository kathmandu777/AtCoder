n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

ans = 0

for i in range(n):
    if a[i][0] < a[i][1]:
        ans += a[i][0]
    else:
        ans += a[i][1]

print(ans)
