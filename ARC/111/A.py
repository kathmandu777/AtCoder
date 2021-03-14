import math
import numpy as np

n, m = map(int, input().split())
ten = 10 / m
len_ten = len(str(ten))
if (len_ten > n):
    ten = str(ten)[:n + 1]
x = ten << 10**len_ten
print(x % m*(x-len_ten))
#print(x % m)
