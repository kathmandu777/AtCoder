import math
d, t, s = map(int, input().split())

num = math.ceil(d/s)
print("Yes" if num <= t else "No")
