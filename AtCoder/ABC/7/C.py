import queue
import sys

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = []
for h in range(H):
    maze.append(input())
# print(maze)

move = ((-1, 0), (1, 0), (0, -1), (0, 1))
visited = [[0] * W for _ in range(H)]

q = queue.Queue()
q.put((sx - 1, sy - 1, 0))

while not q.empty():
    x, y, d = q.get()
    if x + 1 == gx and y + 1 == gy:
        print(d)
        sys.exit()
    if visited[y][x] == 1:
        continue
    else:
        visited[y][x] = 1
        for dx, dy in move:
            if (0 <= x + dx < W) and (0 <= y + dy < H):
                if visited[y + dy][x + dx] == 0 and maze[y + dy][x + dx] == '.':
                    q.put((x+dx, y+dy, d+1))
