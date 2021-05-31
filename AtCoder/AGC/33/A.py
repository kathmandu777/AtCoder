import queue
import sys


def main():
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]

    q = queue.Queue()
    is_white = [[1] * W for _ in range(H)]

    first_black = 0
    for h in range(H):
        for w in range(W):
            if (field[h][w] == "#"):
                q.put((h, w, 0))
                first_black += 1

    if (first_black == H * W):
        print(0)
        sys.exit()

    while not q.empty():
        h, w, count = q.get()
        # if (sum(map(sum, is_white)) == 0):
        #     print(count)
        #     sys.exit()
        if (is_white[h][w] == 0):
            continue

        is_white[h][w] = 0
        for dh, dw in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (0 <= h + dh < H) and (0 <= w + dw < W):
                if(is_white[h + dh][w + dw] == 1):
                    q.put((h + dh, w + dw, count + 1))
    print(0)


if __name__ == "__main__":
    main()
