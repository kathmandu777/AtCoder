n = int(input())
fx = [int(input()) for _ in range(n)]

INF = 9999999999999999
min_fx = fx[0]
ans = -INF

for i in range(n-1):
    ans = max(ans, fx[i+1]-min_fx)
    min_fx = min(min_fx, fx[i+1])


print(ans)
