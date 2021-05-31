n, m, q = map(int, input().split())

Mli = [0] + [n] * m
Nli = [[0] for j in range(n+1)]

for i in range(q):
    que = list(map(int, input().split()))
    if (que[0] == 1):
        ans = 0
        for j in Nli[que[1]]:
            ans += Mli[j]
        print(ans)
    else:
        Mli[que[2]] -= 1
        Nli[que[1]].append(que[2])
