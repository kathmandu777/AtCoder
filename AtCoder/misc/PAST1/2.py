n = int(input())
li = []
for i in range(n):
    li.append(int(input()))


for i in range(1, len(li)):
    if (li[i] == li[i - 1]):
        print("stay")
    elif (li[i] > li[i - 1]):
        print("up", li[i] - li[i - 1])
    else:
        print("down", li[i - 1] - li[i])
