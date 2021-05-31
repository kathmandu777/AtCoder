N = int(input())
students = list(map(int, input().split()))
schools = list(map(int, input().split()))

students.sort()
schools.sort()

ans = 0
for i in range(N):
    ans += abs(students[i] - schools[i])

print(ans)
