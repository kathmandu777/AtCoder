import math


n, x, t = map(int, input().split())

ans = math.ceil(n/x)

print(ans*t)
