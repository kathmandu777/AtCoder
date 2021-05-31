# 再帰関数による実装


import sys
sys.setrecursionlimit(10 ** 7)
# ↑重要
"""
再起数の上限を上げる必要がある
"""


def dfs(y, x):
    if (x < 0 or x >= W):
        return
    if (y < 0 or y >= H):
        return
    if (maze[y][x] == "#"):
        return
    if (maze[y][x] == "g"):
        print("Yes")
        sys.exit()

    maze[y][x] = "#"
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
