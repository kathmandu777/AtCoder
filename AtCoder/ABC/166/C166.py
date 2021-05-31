n, m = map(int, input().split())
h = list(map(int, input().split()))
ansa, ansb = 0, 0
ls = [0]*n

for _ in range(m):
    a, b = map(int, input().split())
    ansa = h[a-1]
    ansb = h[b-1]

    if ansa > ansb:
        ls[b-1] += 1

    elif ansa == ansb:
        ls[a-1] += 1
        ls[b-1] += 1

    else:
        ls[a-1] += 1

print(ls.count(0))
