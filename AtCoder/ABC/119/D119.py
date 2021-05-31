"""
import numpy as np

a, b, q = map(int, input().split())

def getNearestValue(list, num):
    
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]

def getNearestValue(data, target):

    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]
    min_diff = float('inf')
    imin = 0
    imax = len(data) - 1
    closest_num = None
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        #　中心の左右の値と目標との差を計算する。
        if imid + 1 < len(data):
            min_diff_right = abs(data[imid+1] - target)
        if imid > 0:
            min_diff_left = abs(data[imid-1] - target)
        # 最初の差と最も最小に近い値を更新する。
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = data[imid-1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = data[imid+1]
        # 2分探索する。
        if data[imid] < target:
            imin = imid + 1
        elif data[imid] > target:
            imax = imid - 1
        else:
            return data[imid]
    return closest_num


def checkshrine(x):
    x_near_sh = getNearestValue(sh, x)
    xsash = np.abs(x_near_sh - x)
    sh_near_te = getNearestValue(te, x_near_sh)
    return xsash + np.abs(sh_near_te - x_near_sh)


def checktemple(x):
    x_near_te = getNearestValue(te, x)
    xsate = np.abs(x_near_te - x)
    te_near_sh = getNearestValue(sh, x_near_te)
    return xsate + np.abs(te_near_sh - x_near_te)


sh = [int(input()) for _ in range(a)]
te = [int(input()) for _ in range(b)]


for i in range(q):
    x = int(input())
    checkshrinevalue = checkshrine(x)
    checktemplevalue = checktemple(x)
    if (checkshrinevalue > checktemplevalue):
        print(checktemplevalue)
    else:
        print(checkshrinevalue)
"""

import bisect
A, B, Q = map(int, input().split())
INF = 10 ** 18
s = [-INF] + [int(input()) for i in range(A)] + [INF]
t = [-INF] + [int(input()) for i in range(B)] + [INF]
for q in range(Q):
    x = int(input())
    b, d = bisect.bisect_right(s, x), bisect.bisect_right(t, x)
    res = INF
    for S in [s[b - 1], s[b]]:
        for T in [t[d - 1], t[d]]:
            d1, d2 = abs(S - x) + abs(T - S), abs(T - x) + abs(S - T)
            res = min(res, d1, d2)
    print(res)
