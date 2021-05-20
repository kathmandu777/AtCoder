from math import gcd


def lcm(a, b):
    return a // gcd(a, b) * b


a, b = map(int, input().split())
ans = lcm(a, b)
if ans > 1000000000000000000:
    print("Large")
else:
    print(ans)
