import sys

s = input()
t = input()

for i in range(len(s)):
    if (s[i] == t[i]):
        pass
    else:
        print("No")
        sys.exit()

print("Yes")
