import math
import sys

a, b, c = map(int, input().split())
k = int(input())

for i in range(k):
    if (not (b > a)):
        b *= 2
    elif (not (c > b)):
        c *= 2

if (c > b and b > a):
    print("Yes")
else:
    print("No")
