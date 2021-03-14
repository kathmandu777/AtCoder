x, y, a, b = map(int, input().split())

exp = 0
while (y > x):
    pa = x * a
    pb = x + b
    if (pa > pb):
        x = pb
    else:
        x = pa
    exp += 1

print(exp-1)
