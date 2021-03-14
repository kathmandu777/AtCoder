import math
n, k = map(int, input().split())
d = list(input().split())


for i in range(n, n + 1000000000000):
    #各桁を確かめる
        str_i = str(i)
        if str_i[0] in d:
            continue
        if len(str(i))>=2:
            if str_i[1] in d:
                continue
        if len(str(i))>=3:
            if str_i[2] in d:
                continue
        if len(str(i))>=4:
            if str_i[3] in d:
                continue
        if len(str(i))>=5:
            if str_i[4] in d:
                continue
        print(i)
        break