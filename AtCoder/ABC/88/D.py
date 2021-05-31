import queue
import itertools
import sys

H, W = map(int, input().split())
maze = [input() for _ in range(H)]

q = queue.Queue()
q.put((0, 0, 0))
visited = [[0] * W for _ in range(H)]


while not q.empty():
    h, w, d = q.get()

    if (h == H - 1 and w == W - 1):
        count_block = list(itertools.chain.from_iterable(maze)).count("#")
        ans = H*W-count_block-d-1
        print(ans)
        sys.exit()
    if (visited[h][w] == 1):
        continue

    visited[h][w] = 1
    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        if ((0 <= w + dx < W) and (0 <= h + dy < H)):
            if visited[h + dy][w + dx] == 0 and maze[h + dy][w + dx] == '.':
                q.put((h + dy, w + dx, d + 1))


print(-1)
