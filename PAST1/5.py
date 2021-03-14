s = input()

strli = []
pre = -1
for i in range(len(s)):
    if (s[i].isupper()):
        if (pre != -1):
            strli.append(s[pre:i + 1])
            pre = -1
        else:
            pre = i

strli2 = []
for i in strli:
    strli2.append(i.lower())

strli2.sort()

ans = ""
for i in strli2:
    ans = ans + (i[0].upper() + i[1:-1]+i[-1].upper())

print(ans)
