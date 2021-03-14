import math
import sys

n, m = map(int, input().split())

inputlist = []
for _ in range(n):
    inputlist.append([])

for _ in range(m):
    a, b = map(int, input().split())
    inputlist[a-1].append(b)
    inputlist[b-1].append(a)

# 実装

ans = [-1] * n


def check(liin):
    for i in inputlist[liin]:
        if (ans[i - 1] == -1):
            ans[i - 1] = liin+1


for inputindex in range(n):
    dfslist = []
    for liin in inputlist[inputindex]:
        if (ans[liin-1] == -1):
            ans[liin - 1] = inputindex + 1
            dfslist.append(liin)
    for i in dfslist:
        check(i-1)


print("Yes")
ans.pop(0)
for i in ans:
    print(i)
