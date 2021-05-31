x, y = map(int, input().split())

if (x < y and x + 3 > y):
    print("Yes")
elif (y < x and y + 3 > x):
    print("Yes")
else:
    print("No")
