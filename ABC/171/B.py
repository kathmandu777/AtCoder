n, k = map(int, input().split())

list = list(map(int, input().split()))

list.sort()

ans = 0
for i in range(k):
    ans += list[i]
print(ans)
