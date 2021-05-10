ans = 0
for _ in range(20):
    data = list(map(int, input().split()))
    for i in data:
        if i == 1:
            continue
        elif i == 2:
            ans += 1
        else:
            d = 0
            for k in range(1, i):
                if not i % k:
                    d += 1
            if d == 1:
                ans += 1

print(ans)
