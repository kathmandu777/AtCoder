# スタックによる実装
# dfs

from collections import deque


h, w = map(int, input().split())
maze = []
for i in range(h):
    maze.append(input())

for x in range(w):
    for y in range(h):
        if(maze[y][x] == "s"):
            start_x, start_y = x, y

stack = deque([[start_x, start_y]])
visited_list = [[0]*w for _ in range(h)]
visited_list[start_y][start_x] = 1


def dfs(maze, visited_list, stack):
    while len(stack) > 0:
        x, y = stack.pop()
        if maze[y][x] == "g":
            return "Yes"
        for i, j in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_x, new_y = x + i, y + j
            if new_x < 0 or new_x >= w or new_y < 0 or new_y >= h:
                continue
            if maze[new_y][new_x] != "#" and visited_list[new_y][new_x] == 0:
                stack.append([new_x, new_y])
                visited_list[new_y][new_x] = 1
    return "No"


print(dfs(maze, visited_list, stack))
