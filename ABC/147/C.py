n = int(input())
ans = 0
pr = [[] for i in range(n)]
for i in range(n):
    for j in range(int(input())):
        xy = list(map(int, input().split()))
        pr[i].append(xy)

# print(pr)

for i in range(2 ** n):
    tflist = [0]*n  # 全員嘘つきと仮定　0＝嘘つき
    for j in range(n):
        if ((i >> j) & 1):
            tflist[j] = 1
    # print(tflist)
    mujun = False
    for k in range(n):
        if (tflist[k] == 1):
            # print(k)
            for m in pr[k]:
                # print(m)
                #print(tflist[m[0] - 1], m[1])
                if (tflist[m[0] - 1] != m[1]):
                    # print("mujun")
                    mujun = True
                    break
    if (not (mujun)):
        ans = max(ans, tflist.count(1))
        # print("anschange")

    # print()

print(ans)
