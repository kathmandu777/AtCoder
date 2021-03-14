h, w = map(int, input().split())
s = list(input() for _ in range(h))
ans = 0

for i in range(h):
    for j in range(w-1):
        if s[i][j] == "." and s[i][j+1] == ".":
            ans += 1

for i in range(w):
    for j in range(h-1):
        if s[j][i] == "." and s[j+1][i] == ".":
            ans += 1

print(ans)
