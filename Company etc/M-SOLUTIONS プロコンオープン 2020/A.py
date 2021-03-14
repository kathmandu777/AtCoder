import math
import sys


n = int(input())

if n >= 400 and n < 600:
    print(8)

elif n >= 600 and n < 800:
    print(7)

elif n >= 800 and n < 1000:
    print(6)

elif n >= 1000 and n < 1200:
    print(5)

elif n >= 1200 and n < 1400:
    print(4)

elif n >= 1400 and n < 1600:
    print(3)

elif n >= 1600 and n < 1800:
    print(2)

else:
    print(1)
