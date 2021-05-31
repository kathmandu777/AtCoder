import math
import sys
import numpy
import itertools
import copy

import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())

ans = 0
for i in range(1, 8):
    if (n >= 10 ** (i * 3)):
        ans += min(999 * 10 ** (i * 3) * i, (n - 10 ** (i * 3) + 1) * i)


print(ans)
