import sys
from collections import deque

n, m, k = map(int, input().split())
Alist = deque()
Blist = deque()
Alist.extend(list(map(int, input().split())))
Blist.extend(list(map(int, input().split())))

sum = 0
book = 0
while (True):
    if (len(Alist) == 0):
        while (True):
            if (len(Blist) == 0):
                print(book)
                sys.exit()
            if (k - Blist[0] >= 0):
                k -= Blist[0]
                Blist.popleft()
                book += 1
            else:
                print(book)
                sys.exit()
    elif(len(Blist) == 0):
        while (True):
            if (len(Alist) == 0):
                print(book)
                sys.exit()
            if (k - Alist[0] >= 0):
                k -= Alist[0]
                Alist.popleft()
                book += 1
            else:
                print(book)
                sys.exit()

    if (Alist[0] < Blist[0]):
        if (k - Alist[0] >= 0):
            k -= Alist[0]
            Alist.popleft()
            book += 1
            # print(k)
        else:
            break
    else:
        if (k - Blist[0] >= 0):
            k -= Blist[0]
            Blist.popleft()
            book += 1
            # print(k)
        else:
            break

print(book)
