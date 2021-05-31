N = int(input())
A, B, C = map(int, input().split())

ans = 999999999999
for i in range(10000):
    for j in range(10000 - i):
        tmp = (N - A * i - B * j)
        if(tmp < 0):
            break
        k = tmp / C
        # print(i, j, k)
        if(k.is_integer()):
            ans = min(i + j + k, ans)
            # print(ans)
print(int(ans))
