import itertools
import copy

li = [int(s) for s in list(input())]
first_li = copy.copy(li)


for h in range(20, 0, - 1):
    for i in list(itertools.combinations(li, h)):
        if (sum(i) % 3 == 0):
            # print(i)
            if (set(i) <= set(li)):
                for j in range(len(i)):
                    #print(li, i[j])
                    li.remove(i[j])
# print(li)
if (first_li == li):
    print(-1)
else:
    print(len(li))
