# 再帰関数による実装
# 計算量：O(N+M)  頂点数N、辺数Mとする

# https: // atcoder.jp/contests/atc001/tasks/dfs_

import sys
sys.setrecursionlimit(10 ** 7)
"""
再起数の上限を上げる必要がある
"""


def dfs(y, x):
    if (x < 0 or x >= W or y < 0 or y >= H):  # 範囲外であればreturn
        return
    if (maze[y][x] == "#"):  # 探索不可（行き止まりや壁など）であればreturn
        return
    if (maze[y][x] == "g"):  # 最終目標であれば終了
        print("Yes")
        sys.exit()

    maze[y][x] = "#"  # 到達済みであることを記す

    # 各方向へ再帰的?に関数呼び出し
    dfs(y, x + 1)
    dfs(y + 1, x)
    dfs(y, x - 1)
    dfs(y - 1, x)


if __name__ == '__main__':
    H, W = map(int, input().split())
    maze = [list(input()) for i in range(H)]
    # print(maze)

    visited = []
    for h in range(H):
        for w in range(W):
            if (maze[h][w] == "s"):
                dfs(h, w)

print("No")
