import bisect

N = int(input())
classes = list(map(int, input().split()))
Q = int(input())
students = [0] * Q
for i in range(Q):
    students[i] = int(input())

# print(classes)
# print(students)

classes.sort()
for i in range(Q):
    j = bisect.bisect(classes, students[i])
    if j == 0:
        print(abs(students[i] - classes[j]))
        continue
    if j == N:
        print(abs(students[i] - classes[j - 1]))
        continue
    if (abs(students[i] - classes[j]) > abs(students[i] - classes[j - 1])):
        print(abs(students[i] - classes[j - 1]))
    else:
        print(abs(students[i] - classes[j]))
