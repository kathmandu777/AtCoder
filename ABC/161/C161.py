import sys
import math

n, k = map(int, input().split())

pre=abs(n-n//k*k)

while 1:
    if pre <= abs(pre-k):
        print(pre)
        sys.exit()
    pre = abs(pre - k)









