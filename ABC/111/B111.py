list = [111, 222, 333, 444, 555, 666, 777, 888, 999]

n = int(input())
ans={}
for i in list:
    if i-n>=0:
        ans[i]=(i - n)
print(min(ans))