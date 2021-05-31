li = list(map(int, input().split()))
li.remove(max(li))
li.remove(max(li))

print(max(li))
