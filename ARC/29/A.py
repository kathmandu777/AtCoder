n = int(input())
meat = []
for i in range(n):
    meat.append(int(input()))

ans = 9999999999999

for i in range(2 ** n):
    fire1 = []
    fire2 = []
    for j in range(n):
        if ((i >> j) & 1):
            fire1.append(meat[j])
        else:
            fire2.append(meat[j])

    ans = min(ans, max(sum(fire1), sum(fire2)))

print(ans)
