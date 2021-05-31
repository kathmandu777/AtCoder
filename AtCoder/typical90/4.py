H, W = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(H)]

# print(table)
rsum = [sum(r) for r in table]
csum = [sum(c) for c in zip(*table)]


ans = []
for h in range(H):
    child_ans = []
    for w in range(W):
        child_ans.append(csum[w] + rsum[h] - table[h][w])
    ans.append(child_ans)

for r in ans:
    print(*r)
