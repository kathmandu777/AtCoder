n = int(input())
a = [int(x) for x in input().split()]

point_i = 0
current_x = 0
i_max = 0
ans = 0

for i in a:
    point_i += i
    i_max = max(i_max, point_i)
    ans = max(ans, i_max + current_x)
    current_x += point_i

print(ans)
