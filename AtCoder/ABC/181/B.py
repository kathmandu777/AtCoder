n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

sum = 0
for i in range(n):
    sum += 0.5*(li[i][1]-li[i][0]+1)*(2*li[i][0]+((li[i][1]-li[i][0])))

print(int(sum))
