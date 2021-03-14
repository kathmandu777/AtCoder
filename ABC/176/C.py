import math
import sys
"""
n = int(input())
a = list(map(int, input().split()))
"""
n = int(input())
alist = list(map(int, input().split()))
num = 0
ans = 0

for i in alist:
    if num < i:
        num = i
    ans += abs(num-i)
print(ans)
