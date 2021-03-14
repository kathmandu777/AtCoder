N = int(input())
N = 1000 - N

ans = 0
while N > 0:
    for i in (500, 100, 50, 10, 5, 1):
        if (N - i >= 0):
            N -= i
            ans += 1
            break

print(ans)
