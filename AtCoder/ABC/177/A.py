import sys

s = input()
t = input()

finalans = 1000000
for i in range(len(s) - len(t) + 1):
    ans = 0
    for j in range(len(t)):
        if (s[i+j] == t[j]):
            pass
        else:
            ans += 1
    finalans = min(finalans, ans)

print(finalans)
