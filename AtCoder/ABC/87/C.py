n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

sum_list = []
for i in range(n):
    sum_list.append(sum(a1[:(i + 1)]) + sum(a2[(i):]))


print(max(sum_list))
