
import sys
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, input().split())


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)  # 再帰定義


cut_times = gcd(a, gcd(b, c))
# print(cut_times)
print(a // cut_times + b // cut_times + c // cut_times - 3)
