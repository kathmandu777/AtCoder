n = int(input())
begin_last = []
for i in range(n):
    x, l = map(int, input().split())
    begin_last.append([x-l, x + l])

begin_last.sort(key=lambda x: x[1])

ans = 0

pre_last = -999999999999999999
for begin, last in begin_last:
    if (pre_last <= begin):
        ans += 1
        pre_last = last

print(ans)
