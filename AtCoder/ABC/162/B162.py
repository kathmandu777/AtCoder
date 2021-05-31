import math
import sys

n=int(input())
#  =map(int,input().split())
#  =list(map(int,input().split()))

sum=0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        pass
    else:
        sum+=i

print(sum)