
import sys
sys.setrecursionlimit(10 ** 7)


def main():
    w, h = map(int, input().split())
    all_map = []
    while h != 0 and w != 0:
        child_map = []
        for i in range(h):
            child_map.append(list(map(int, input().split())))
        all_map.append(child_map)
        w, h = map(int, input().split())

    for i in range(len(all_map)):
        child_map = all_map[i]
        ans = 0
        for h in range(len(child_map)):
            for w in range(len(child_map[0])):
                if (child_map[h][w] == 1):  # 1が陸
                    dfs(h, w, child_map)
                    ans += 1
        print(ans)


def dfs(h, w, child_map):
    if (h < 0 or h >= len(child_map) or w < 0 or w >= len(child_map[0])):
        return
    if (child_map[h][w] == 0 or child_map[h][w] == 2):
        return

    child_map[h][w] = 2
    dfs(h+1, w, child_map)
    dfs(h-1, w, child_map)
    dfs(h, w+1, child_map)
    dfs(h, w-1, child_map)
    dfs(h+1, w+1, child_map)
    dfs(h-1, w-1, child_map)
    dfs(h-1, w+1, child_map)
    dfs(h+1, w-1, child_map)


if __name__ == "__main__":
    main()
