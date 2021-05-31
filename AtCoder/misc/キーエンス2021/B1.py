import sys
import collections

n, k = map(int, input().split())
a = list(map(int, input().split()))

a_colec = collections.Counter(a)

ans = 0
for i in range(n):
    try:
        if (i == 0):
            if (a_colec[i] > k):
                pre = k
                ans += pre
            else:
                pre = a_colec[i]
                ans += pre
        else:
            if (pre < a_colec[i]):
                ans += pre
            else:
                ans += a_colec[i]
                pre = a_colec[i]
    except:
        pass

print(ans)
