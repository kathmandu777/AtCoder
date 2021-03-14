n, m, q = map(int, input().split())

# つながりのリスト
link = [[] for j in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    link[u].append(v)
    link[v].append(u)

color = list(map(int, input().split()))
color.insert(0, -1)

for i in range(q):
    query = list(map(int, input().split()))
    if (query[0] == 1):
        print(color[query[1]])
        for j in link[query[1]]:
            color[j] = color[query[1]]
    else:
        print(color[query[1]])
        color[query[1]] = query[2]
