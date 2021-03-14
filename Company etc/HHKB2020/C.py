from collections import deque

n = int(input())
p = list(map(int, input().split()))

num = [0] * (n + 10)

for i in range(n):
    num[p[i]] = 1
    print(num.index(0))
