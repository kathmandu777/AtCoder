n = int(input()) 
d = []
for i in range(n):
    d.append(int(input()))

d.sort()
before = 0
ans=0
for i in d:
    if i >= before:
        ans += 1
    else:
        break
    before = i
    
print(ans)