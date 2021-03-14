import sys

n = int(input())
for i in range(10000):
    if (i * 1000 - n >= 0):
        print(i * 1000 - n)
        sys.exit()
