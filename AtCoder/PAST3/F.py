import collections
import sys

n = int(input())
s = []

for _ in range(n):
    s.extend(list(input()))

s = collections.Counter(s)
countlitup = s.most_common()

countli = []
for i in countlitup:
    countli.append(list(i))

ansli = []
ansone = -1
if(countli[-1][1] == 1):  # 1つのみある文字を抽出
    ansone = countli[-1][0]

lencount = 0
while len(countli) > 0:  # 二つある文字をなくなるまで抽出
    if (countli[0][1] >= 2):
        ansli.append(countli[0][0])
        lencount += 1
        countli[0][1] -= 2
    else:
        countli.pop(0)

if (n % 2 == 1 and ansone == -1):
    print(-1)
    sys.exit()
elif (lencount == 0):
    print(-1)
    sys.exit()

if (n % 2 == 1):  # ansoneが定義されていれば
    ans = ["-1"] * n
    ans[n//2] = ansone
    for i in range(n//2):
        ans[i] = ansli[0]
        ans[-(i+1)] = ansli[0]
        ansli.pop(0)
else:
    ans = ["-1"]*n
    for i in range(n//2):
        ans[i] = ansli[0]
        ans[-1] = ansli[0]
        ansli.pop(0)

print("".join(ans))
