import copy

n = int(input())
a = list(map(int, input().split()))
first_a = copy.deepcopy(a)
for i in range(n-1):
    next = []
    for j in range(0, len(a), 2):
        next.append(max(a[j], a[j + 1]))
    a = next
    # print(a)


print(first_a.index(min(a))+1)
