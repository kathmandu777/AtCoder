# ビット全探索
# 計算量：O(N*2^N)
# https://atcoder.jp/contests/arc029/tasks/arc029_1

n = int(input())
meat = []
for i in range(n):
    meat.append(int(input()))

ans = 9999999999999

for i in range(2 ** n):  # 2^n通りまわす
    fire1 = []
    fire2 = []
    for j in range(n):  # 各bitについてみていく
        if ((i >> j) & 1):  # bitがたっていたら
            fire1.append(meat[j])
        else:
            fire2.append(meat[j])

    ans = min(ans, max(sum(fire1), sum(fire2)))

print(ans)
