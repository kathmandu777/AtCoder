import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

box = [0] * k

ans = 0
for i in range(n):
    for j in range(k):
        if (j == 0):
            tmp = a.pop()
            ans += 1
            #print(ans, a)
            if (len(a) == 0):
                print(ans)
                sys.exit()
            continue
        if (tmp == a[-1]):
            a.pop()
            ans += 1
            #print(ans, a)
            if (len(a) == 0):
                print(ans)
                sys.exit()
        else:
            k = j
            break

    while (a[-1] == tmp):
        a.pop()
        if (len(a) == 0):
            print(ans)
            sys.exit()

print(ans)
