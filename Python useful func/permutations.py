# 順列を計算します


def permutations_count(n, r):
    ans = 1
    for i in range(r):
        ans *= (n - i)
    return ans


print(permutations_count(5, 2))
