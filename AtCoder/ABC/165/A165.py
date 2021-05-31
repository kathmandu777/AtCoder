import sys
k = int(input())
a, b = map(int, input().split())

for i in range(1000):
    if (k * i >= a and k * i <= b):
        print("OK")
        sys.exit()
    else:
        pass
print("NG")
