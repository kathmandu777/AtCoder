import numpy as np

sx, sy, gx, gy = map(int, input().split())

gy = -gy
a = (gy - sy) / (gx - sx)
b = -a * sx + sy
ans = -b / a
print('{:.10f}'.format(ans))
