n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
middle = []
if (n % 2 == 0):
    middle = a[:n // 2]
    # print(middle)

    sum = sum(middle)-middle[-1]
    for i in range(n // 2-1):
        sum += middle[i + 1]
    sum += middle[-1]
else:
    middle = a[:n // 2+1]
    # print(middle)

    sum = sum(middle)-middle[-1]
    for i in range(n // 2):
        sum += middle[i+1]
print(sum)
