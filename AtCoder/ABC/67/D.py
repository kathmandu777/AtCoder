import sys
N = int(input())
sys.setrecursionlimit(N+10)

es = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    es[a].append(b)
    es[b].append(a)

"""
相手の取れるマス目を減らすようにとるとよい
相手よりそのマスに近ければそのマスを取得できる
フェネックくん、すぬけ君について初期地点からそれぞれへの距離が必要
"""


def solve(now, depth, depth_list, es, visited):
    visited[now] = True
    depth_list[now] = depth
    for next in es[now]:
        if visited[next] == False:
            solve(next, depth+1, depth_list, es, visited)


depth_list_F = [0] * N
visited_F = [False] * N
solve(0, 0, depth_list_F, es, visited_F)

depth_list_S = [0] * N
visited_S = [False] * N
solve(N-1, 0, depth_list_S, es, visited_S)

cnt_F = cnt_S = 0
for f, s in zip(depth_list_F, depth_list_S):
    if f <= s:
        cnt_F += 1  # フェネック君から始めるので同じ距離ならフェネック君がとる
    else:
        cnt_S += 1

if cnt_F > cnt_S:
    print("Fennec")
else:
    print("Snuke")
