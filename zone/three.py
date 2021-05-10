n, m = map(int, input().split())
g = [set() for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)
print(g)
ans = []
max = 0
for i in range(50):
    for j in range(i):
        for k in range(j):
            m = len(g[i] | g[j] | g[k])
            if max < m:
                max = m
                ans = [i, j, k]
print(ans, max)
