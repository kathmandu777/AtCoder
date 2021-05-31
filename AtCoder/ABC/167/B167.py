import sys

a, b, c, k = map(int, input().split())
sum = 0

if a <= k:
    sum += a
    k -= a

else:
    sum += k
    print(sum)
    sys.exit()

k -= b

if k > 0:
    sum += -1*k

print(sum)
