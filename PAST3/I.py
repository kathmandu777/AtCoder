import numpy as np

n = int(input())
q = int(input())

a = np.arange(n * n).reshape((n, n))
for i in range(q):
    query = list(map(int, input().split()))
    if (query[0] == 2):
        if (query[1] == query[2]):
            pass
        else:
            retu = list(range(n))
            retu[query[1] - 1] = query[2]-1
            retu[query[2] - 1] = query[1]-1
            a = a[:, retu]
    elif (query[0] == 1):
        if (query[1] == query[2]):
            pass
        else:
            gyou = list(range(n))
            gyou[query[1] - 1] = query[2]-1
            gyou[query[2] - 1] = query[1] - 1
            a = a[gyou, :]
    elif (query[0] == 3):
        a = a.T
    else:
        print(a[query[1] - 1, query[2] - 1])
