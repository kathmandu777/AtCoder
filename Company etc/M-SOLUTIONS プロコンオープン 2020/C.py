n, k = map(int, input().split())
li = list(map(int, input().split()))

for i in range(n-k):
    if li[i] >= li[i+k]:
        print("No")
    else:
        print("Yes")
