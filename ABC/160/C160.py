import sys

k,n=map(int,input().split())
a=list(map(int,input().split()))

  
b=[]
b.append(k+a[0]-a[n-1])

for i in range(n-1):
    b.append(abs(a[i+1]-a[i]))

b.remove(max(b))

print(sum(b))

