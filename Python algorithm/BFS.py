# BFSのqueueによる実装
# 計算量：O(N+M)  頂点数N、辺数Mとする

# https://atcoder.jp/contests/abc007/tasks/abc007_3

import queue
import sys

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = []
for h in range(H):
    maze.append(input())

visited = [[0] * W for _ in range(H)]

q = queue.Queue()
q.put((sx - 1, sy - 1, 0))  # 始点の(x,y)とコストd

while not q.empty():  # キューが空になるまで無限に回す
    x, y, d = q.get()  # キューにある者の中から一番最初に入れられたものを取り出す（FIFO）
    if x + 1 == gx and y + 1 == gy:  # 最終目標であったら終了
        print(d)
        sys.exit()
    if visited[y][x] == 1:  # 以前に到達していたらcontinue
        continue
    else:
        visited[y][x] = 1  # 到達済みであることを記す
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 各方向を探索
            if (0 <= x + dx < W) and (0 <= y + dy < H):  # 範囲内であれば
                if visited[y + dy][x + dx] == 0 and maze[y + dy][x + dx] == '.':  # 未到達 and 探索可能であれば
                    q.put((x+dx, y+dy, d+1))  # キューに追加(enqueue)
