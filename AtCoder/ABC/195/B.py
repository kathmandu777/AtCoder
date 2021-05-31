import math

a, b, w = map(int, input().split())
w = w * 1000
min_val = math.ceil(w / b)
max_val = math.floor(w / a)
if(a <= w / min_val and w / min_val <= b and a <= w / max_val and w / max_val <= b):
    print(min_val, max_val)
else:
    print("UNSATISFIABLE")
