import math
import sys
a, b, c, d = map(int, input().split())

while 1:
    if (c > 0):
        c -= b
    if(c <= 0):
        print("Yes")
        sys.exit()
    if (a > 0):
        a -= d
    if(a <= 0):
        print("No")
        sys.exit()
