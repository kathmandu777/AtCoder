# いもす法（累積和）
# https: // takeg.hatenadiary.jp / entry / 2019 / 08 / 28 / 213526


# ABC183 D

import sys
n, w = map(int, input().split())
stp = []
for i in range(n):
    stp.append(list(map(int, input().split())))


data = [0] * (10**6)
for i in range(n):
    data[stp[i][0]] += stp[i][2]
    data[stp[i][1]] -= stp[i][2]

ans_data = []
check = 0
for i in range(len(data)):
    check += data[i]
    if check > w:
        print("No")
        sys.exit()

print("Yes")
