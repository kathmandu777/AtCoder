n=int(input())
list=[]

for i in range(1,n+1):
    list.append(i)

answer=[]
answer=[i for i in list if i%2!=0]
ans=len(answer)/n
print("%012.10f" %ans)