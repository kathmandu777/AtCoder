N=int(input())
H = list(map(int, input().split())) 

count=[0]
count_index=0
index=0

while index < N-1:        #すべての値を調査し終わるまで
    if(H[index] >= H[index+1]):#続いている
        count[count_index]+=1
        index+=1

    else:       #続かなくなったら
        count_index+=1
        count.append(0)
        index+=1

        
ans=0
for i in range(len(count)):
    if(ans<count[i]):
        ans=count[i]

        
print(ans)
