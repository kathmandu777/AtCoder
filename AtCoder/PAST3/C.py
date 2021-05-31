a, r, n = map(int, input().split())

if ((a * r ** (n - 1)) > 10 ** 9):
    print("large")
else:
    print(a * r ** (n - 1))
