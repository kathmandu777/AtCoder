import math

x = int(input())
money = 100
y = 1

while 1:
    if (math.floor(money * 1.01) >= x):
        print(y)
        break
    else:
        y += 1
        money = math.floor(money * 1.01)
