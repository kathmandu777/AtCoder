import copy
import sys
import itertools
sys.setrecursionlimit(10 ** 7)


def main():
    island = [list(input()) for _ in range(10)]

    tmp_island = copy.deepcopy(island)
    flg = False
    for h in range(10):
        for w in range(10):
            if (island[h][w] == "o"):
                dfs(h, w, tmp_island)
                for k in tmp_island:
                    print(k)
                # tmp_islandに"o"が含まれていたら
                if ({"o"} <= set(tuple(list(itertools.chain.from_iterable(tmp_island))))):
                    flg = True
                else:
                    print("YES")
                    sys.exit()
            if (flg):
                break
        if (flg):
            break

    for h in range(10):
        for w in range(10):
            if (island[h][w] == "x"):
                tmp_island = copy.deepcopy(island)
                tmp_island[h][w] = "o"
                dfs(h, w, tmp_island)
            else:
                continue

            for k in tmp_island:
                print(k)
            print()
            # tmp_islandに"o"が含まれていたら
            if ({"o"} <= set(tuple(list(itertools.chain.from_iterable(tmp_island))))):
                pass
            else:
                print("YES")
                sys.exit()

    print("NO")


def dfs(h, w, tmp_island):
    if (h < 0 or w < 0 or h >= 10 or w >= 10 or tmp_island[h][w] == "x"):
        return
    if (tmp_island[h][w] == "v"):
        return

    tmp_island[h][w] = "v"
    dfs(h, w + 1, tmp_island)
    dfs(h + 1, w, tmp_island)
    dfs(h - 1, w, tmp_island)
    dfs(h, w - 1, tmp_island)


if __name__ == "__main__":
    main()
