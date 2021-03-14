n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
max_a = 0
for i in range(n):
    max_a = max(max_a, a[i])
    ans = max(ans, max_a * b[i])
    print(ans)
