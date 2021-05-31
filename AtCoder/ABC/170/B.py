from numpy import linalg, array
import sys
"""
x, y = map(int, input().split())

for i in range(1, x+1):
    if (i * 2 + (x - i) * 4 == y):
        print(i, x-i)
        print("Yes")
        sys.exit()

print("No")

"""
"""
N, M = map(int, input().split())
for i in range(1, N+1):
    # 足の数
    f = 2 * i + 4 * (N - i)
    if f == M:
        print("Yes")
        break
    else:
        print('No')
"""

"""
N, M = map(int, input().split())
crain = (4 * N - M) / 2
if crain.is_integer() and crain > 0:
    crain = int(crain)
    print("Yes")
else:
    print('No')
"""
A = [[2, 4], [1, 1]]  # それぞれ足と首の数
At = linalg.inv(A)  # 逆行列
Y = array([10, 3])  # 足が10本、首が3本
print(At @ Y)
