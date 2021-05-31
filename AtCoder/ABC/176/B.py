import math
import sys

n = input()

digit_sum = 0
for i in range(len(n)):
    digit_sum += int(n[i])

if (digit_sum % 9 == 0):
    print("Yes")
else:
    print("No")
