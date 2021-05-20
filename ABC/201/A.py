A = list(map(int,input().split()))
A.sort()
ans = "No"
if A[2]-A[1] == A[1]-A[0]:
  ans = "Yes"
print(ans)

