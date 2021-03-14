import math
import sys
import functools
import operator

n = int(input())
a = list(map(int, input().split()))


ans = 1
INF = 1000000000000000000

if (0 in a):
    print(0)
    sys.exit()

for i in a:
    ans *= i
    if(ans > INF):
        print(-1)
        sys.exit()

print(ans)
