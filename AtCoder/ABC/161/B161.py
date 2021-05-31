import sys
import math



n, m = map(int, input().split())
a = list(map(int, input().split()))
sum=sum(a)

for i in range(m):
    if max(a) < (sum/(4*m)):
        
        print("No")
        sys.exit
    else:
        a.remove(max(a))
print("Yes")     