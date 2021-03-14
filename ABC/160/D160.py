#not solve

n,x,y=map(int,input().split())

ls=[]
for i in range(1,n):
    ls.append([i,i+1])
ls.append([x,y])
ls.sort(reverse=True)
print(ls)

print(n)

for k in range(2,n):
    count=0
    for i in range(1,n-1):
        for j in range(1,n-1):
        
                count+=1
    print(count)  







