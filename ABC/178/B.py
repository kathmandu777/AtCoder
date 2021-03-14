import sys

n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
count = 0

for i in range(n):
    if (len(set(li[i])) == 1):
        count += 1
    else:
        count = 0
    if (count == 3):
        print("Yes")
        sys.exit()

print("No")
