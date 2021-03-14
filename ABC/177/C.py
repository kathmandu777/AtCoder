import itertools
import math

n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in itertools.combinations(a, 2):
    ans += ((i[0] % 1000000007)*(i[1] % 1000000007)) % 1000000007

print(ans % 1000000007)
