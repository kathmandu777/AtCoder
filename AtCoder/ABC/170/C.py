import sys

x, n = map(int, input().split())
listdame = list(map(int, input().split()))

for i in range(100):
    if (x - i in listdame):
        pass
    else:
        print(x - i)
        sys.exit()

    if (x + i in listdame):
        pass
    else:
        print(x + i)
        sys.exit()
