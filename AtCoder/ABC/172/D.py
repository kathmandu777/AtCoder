n = []
while True:
    try:
        kari = (input())
        if (kari == "end"):
            break
        else:
            n.append(kari)
    except EOFError:
        break

ans = ""
for i in range(len(n)):
    if (i % 2 == 0):
        ans += n[i]

print(ans)
