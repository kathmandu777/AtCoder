# ユーグリッドの互除法
# Euclidean algorithm

import sys
sys.setrecursionlimit(10 ** 7)


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)  # 再帰定義
