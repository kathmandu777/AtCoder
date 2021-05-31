n, k = map(int, input().split())
a_list = list(map(int, input().split()))

sum_list = [0]
for a in a_list:
    sum_list.append(sum_list[-1] + a)
print(sum_list)

ans = 0
for i in range(n - k + 1):
    ans += sum_list[i + k] - sum_list[i]
print(ans)
