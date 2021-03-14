import math

n = int(input())
x = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += abs(x[i])

print(ans)


ans = 0
for i in range(n):
    ans += (x[i])**2

print(math.sqrt(ans))


ans = []
for i in range(n):
    ans.append(abs(x[i]))
print(max(ans))
