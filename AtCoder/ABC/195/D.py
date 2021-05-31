import copy
import numpy as np
# from icecream import ic

n, m, q = map(int, input().split())
bag = []
for i in range(n):
    w, v = map(int, input().split())
    bag.append([w, v])
bag.sort(key=lambda x: x[1], reverse=True)  # value順でソート
# ic(bag)

const_boxes = list(map(int, input().split()))

query = []
for i in range(q):  # 50
    ans = 0
    boxes = copy.deepcopy(const_boxes)
    l, r = map(int, input().split())
    del boxes[l - 1:r]
    # ic(boxes)
    boxes.sort()  # 小さい順にソート
    for w, v in bag:  # 50
        # ic(w, v)
        if len(boxes) == 0:
            break
        for box in boxes:  # 50
            if box >= w:
                ans += v
                boxes.remove(box)
                break
    print(ans)
