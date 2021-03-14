import sys

n = int(input())

alist = list(map(int, input().split()))
alist.sort()
EncountSosuu = [alist[0]]

# 同じ数のみならば0
if (len(list(set(alist))) == 1):
    print(0)
    sys.exit()


ans = 1

for i in range(1, n):
    isDivide = False
    for j in EncountSosuu:
        if (alist[i] % j == 0):  # 今迄にあった数で割り切れれば
            #print("divide", alist[i], j)
            isDivide = True
            break
    if(not(isDivide)):
        ans += 1
        EncountSosuu.append(alist[i])
        #print("append", alist[i])
    # print()
print(ans)
