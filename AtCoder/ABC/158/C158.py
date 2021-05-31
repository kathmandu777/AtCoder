#解けていない

import sys
import math
import numpy

a,b=map(int,input(.split()))
c=100*a+100*b

for X in numpy.arange(c-100, c+100)
    if(math.floor(8*X)+math.floor(10*X)==c):
        print(X)
        sys.exit(0)

print(-1)






