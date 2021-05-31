import collections
import sys

n = int(input())
s = []

for _ in range(n):
    s.append(list(input()))

doubleli = []
for i in range(n // 2):
    doubleli.append(list(set(s[i]) & set(s[-(i+1)])))
ans = [0] * n
for i in range(n // 2):
    try:
        ans[i] = doubleli[i][0]
        ans[-(i + 1)] = doubleli[i][0]
    except Exception as e:
        print(-1)
        sys.exit()


if (n % 2 == 1):
    ans[n // 2] = s[n // 2][0]

print("".join(ans))
