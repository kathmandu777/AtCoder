import sys

n, k = map(int, input().split())
a = []
a = list(map(int, input().split()))
a = [1] + a
# print(a)

i = 0
ans = [-1]*(2*10**5)
check = 1
for j in range(len(a)):
    if (ans[j]=-1):
        check = 0
        break
    else:
        ans.append(a[(ans[i])])
        i += 1
    if (j == k):
        answer = ans[-1]

if (check == 1):
    print(answer)
    sys.exit()

# print(ans)
delcount = 0
for _ in range(len(ans)):
    if ans[-1] == ans[0]:
        ans.pop(-1)
        break
    else:
        ans.pop(0)
        delcount += 1

#print(ans, delcount)
print(ans[(k-delcount) % len(ans)])
