# 区間スケジューリング
# =>与えられた区間 ( s[j], f[j] ) から，交差しない最大個数の区間集合を求める問題
# 参考：http://uchifuji.hatenablog.com/entry/2017/10/24/045501
# 計算量（平均）：O(n*log(n))

# 問題：https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b


n = int(input())
begin_last = []
for i in range(n):
    x, l = map(int, input().split())
    begin_last.append([x-l, x + l])

begin_last.sort(key=lambda x: x[1])  # 終点を昇順（1,2,3,...）にソート

ans = 0

pre_last = -999999999999999999
for begin, last in begin_last:
    if (pre_last <= begin):  # 始点が前回の終点と重なっていないもののを選ぶ =であることに注意
        ans += 1
        pre_last = last

print(ans)
