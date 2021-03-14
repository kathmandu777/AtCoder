n = int(input())
a = list(map(int, input().split()))
# print(a)
ans = [0] * (1050)

for i in range(2, 1050):
    for j in a:
        #print(j, i)
        if (j % i == 0):
            ans[i] += 1
# print(ans)
print(ans.index(max(ans)))
