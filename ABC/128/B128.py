n = int(input())
sp = []
for i in range(n):
    s, p = map(str, input().split())
    sp.append([s, int(p), i+1])

sp.sort(key=lambda x: x[1], reverse=True)
sp.sort(key=lambda x: x[0])

for e in sp:
    print(e[2])
