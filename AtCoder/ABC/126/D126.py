"""
n = int(input())

li = [0] * n

for i in range(n-1):
    u, v, w = map(int, input().split())
    if w % 2 == 0:
        li[u - 1] += 1
        li[v - 1] += 1

for i in li:
    if i == 0:
        print(1)
    else:
        print(0)
"""


N = int(input())
edges = [list(map(int, input().split())) for _ in range(N - 1)]
print()
print(edges)
print()
A = [[] for _ in range(N+1)]

for edge in edges:
    A[edge[0]].append([edge[1], edge[2]])
    A[edge[1]].append([edge[0], edge[2]])
    print(A)
depth = [-1] * (N+1)
depth[1] = 0


def dfs(A, s):
    print()
    print(depth)
    for v in A[s]:
        print()
        print(A[s], v)
        if depth[v[0]] == -1:
            depth[v[0]] = depth[s] + v[1]
            dfs(A, v[0])
            print("back")


dfs(A, 1)
for d in depth[1:]:
    if d % 2 == 0:
        print(0)
    else:
        print(1)
