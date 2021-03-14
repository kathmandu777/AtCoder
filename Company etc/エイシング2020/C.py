import math
import itertools
import time

start = time.time()
n = int(input())

print("[")
for i in range(1, n + 1):
    ans = 0
    OneToRootn = list(range(1, math.ceil(math.sqrt(i))))
    for xyz in list(itertools.combinations_with_replacement(OneToRootn, 3)):
        if (xyz[0] * xyz[0] + xyz[1] * xyz[1] + xyz[2] * xyz[2]+xyz[0]*xyz[1]+xyz[1]*xyz[2]+xyz[2]*xyz[0] == i):
            lenset = len(set(xyz))
            if (lenset == 1):  # 3つ同じ
                # print(xyz)
                ans += 1
            elif (lenset == 2):
                ans += 3
            else:
                ans += 6
    print(ans, end="")
    print(",")

print("]")
print(time.time() - start)
