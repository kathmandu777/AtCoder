#! 両者ともに計算量は O(log min(a,b))

# LCM(Least common multiple)：最小公倍数
# こちらは自分で実装する必要あり
"""
２つの自然数の積はその最小公倍数と最大公約数の積に等しくなる
a×b=lcm×gcd

を利用
"""
from math import gcd


def lcm(a, b):
    return a // gcd(a, b) * b


# GCD(Greatest common divisor)：最大公約数
gcd(X, Y)
