n, prime_price = map(int, input().split())
a = []
b = []
c = []
for i in range(n):
    A, B, C = map(int, input().split())
    a.append(A)
    b.append(B)
    c.append(C)

a_sort = sorted(a, reverse=True)
b_sort = sorted(b, reverse=True)

ans = 0

delta = a_sort.pop()
if a_sort[-1] < b_sort[-1]:
    delta2 = a_sort.pop()
else:
    delta2 = b_sort.pop()


for i in range(n):
    delta_price = 0
    print(delta, delta2)
    for j in range(n):
        if (a[j] <= delta and delta2 <= b[j]):
            delta_price += c[j]

    ans += min(delta_price, prime_price)
    # print(ans)
    if (b_sort[-1] == delta2):
        break
    delta = delta2
    print(a_sort, b_sort)
    if (len(a_sort) == 0):
        delta2 = b_sort.pop()
    else:
        if a_sort[-1] < b_sort[-1]:
            delta2 = a_sort.pop()
        else:
            delta2 = b_sort.pop()


print(ans)
