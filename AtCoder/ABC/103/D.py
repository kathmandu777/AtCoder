n, m = map(int, input().split())
proposal = [list(map(int, input().split())) for _ in range(m)]

proposal.sort(key=lambda x: x[1])

ans = 0
pre_b = 0
for a, b in proposal:
    if (pre_b <= a):
        ans += 1
        pre_b = b

print(ans)
