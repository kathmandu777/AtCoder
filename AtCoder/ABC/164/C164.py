n = int(input())
li = []
for i in range(n):
    li.append(input())

newli = list(set(li))
print(len(newli))
