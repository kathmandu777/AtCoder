import numpy as np

h, w, k = map(int, input().split())
a = np.full((h, w), "", dtype=str)
for i in range(h):
    a[i] = list(input())

print(a)
