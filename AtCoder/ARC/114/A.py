import numpy as np
# from #icecream import #ic
import collections
import itertools

n = int(input())
x = list(map(int, input().split()))
x.sort()
# ic(x)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


factor = []

for xi in x:
    # ic(xi)
    li = factorization(xi)
    new_li = []
    for li_child in li:
        new_li.append(li_child[0])
    # ic(new_li)
    factor.append(new_li)
    # ic(factor)
modeli = []
while len(factor) != 0:
    # ic(factor)
    factor_co = collections.Counter(
        list(itertools.chain.from_iterable(factor)))
    mode = factor_co.most_common()[0][0]
    # ic(mode)
    modeli.append(mode)
    factor = [factor_child for factor_child in factor if not mode in factor_child]

print(np.prod(np.array(modeli)))
