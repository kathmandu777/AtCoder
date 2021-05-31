N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diff = 0
for i in range(N):
    diff += abs(a[i] - b[i])
# print(diff)

if K - diff >= 0 and (K - diff) % 2 == 0:
    print("Yes")
else:
    print("No")
