#解けていない


a=list(map(int, input().split())) 
b=list(map(int, input().split())) 
c=list(map(int, input().split())) 

sat=0 #satisfaction
mem=-1

for i in a:
    if(mem+1==i):
        sat+=c[i]
    sat+=b[i]
    mem=i

print(sat)