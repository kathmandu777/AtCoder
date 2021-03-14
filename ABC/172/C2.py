from collections import deque

n, m, k = map(int, input().split())
Alist = deque()
Blist = deque()
Alist.extend(list(map(int, input().split())))
Blist.extend(list(map(int, input().split())))

ABlist = deque()
book = 0
nm = n+m
while (len(ABlist) <= nm):
    if (len(Alist) == 0):
        ABlist.extend(Blist)
        break
    elif (len(Blist) == 0):
        ABlist.extend(Alist)
        break

    if (Alist[0] < Blist[0]):
        ABlist.append(Alist[0])
        Alist.popleft()
    else:
        ABlist.append(Blist[0])
        Blist.popleft()

while (len(ABlist) > 0):
    if (k - ABlist[0] >= 0):
        k -= ABlist[0]
        ABlist.popleft()
        book += 1
    else:
        break
print(book)
