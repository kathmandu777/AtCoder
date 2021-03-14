import sys

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
if (len(set(li)) == n):
    print("Correct")
else:
    numdict = []
    for i in range(n):
        numdict.append(i+1)

    removenum = list(set(numdict)-set(li))
    addnum = list([x for x in set(li) if li.count(x) > 1])
    print(addnum[0], removenum[0])
