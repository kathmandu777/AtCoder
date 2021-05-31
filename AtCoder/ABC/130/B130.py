n, x = map(int, input().split())
l = list(map(int, input().split()))

sum = 0
ans = 0

for i in range(n):
    if sum + l[ans] > x:
        break
    sum += l[ans]
    ans += 1

print(ans+1)
