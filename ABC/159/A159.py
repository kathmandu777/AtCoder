import math
n,m=map(int,input().split())

print(math.floor(n * (n - 1) / 2) + math.floor(m * (m - 1)/2))

#これを解くのに11分もかかった　これはひらめき問題
