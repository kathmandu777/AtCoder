n, m, x = map(int, input().split())
INF = 10 ** 18  # 定数は大文字　INF＝Infinity（無限大）
ans = INF
li = []
for i in range(n):
    li.append(list(map(int, input().split())))


for i in range(2 ** n):
    cost = 0
    know = [0]*m  # アルゴリズムM個
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            # フラグが立っていたら
            cost += li[j][0]
            for k in range(m):
                know[k] += li[j][k + 1]

    knowbool = True
    for i in range(m):  # 理解度がXを超えているか
        if (know[i] < x):
            knowbool = False

    if (knowbool):
        ans = min(ans, cost)


if (ans == INF):  # ansが更新されていない　つまりどのパターンをとっても理解度Xを超えなかったら
    print(-1)
else:
    print(ans)
