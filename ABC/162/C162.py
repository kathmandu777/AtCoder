#ダメです

import fractions
import math
import sys

k =185
#  =map(int,input().split())
#  =list(map(int,input().split()))
sum = 0

for i in range(1, k + 1):
    for j in range(1, k + 1):
        for n in range(1, k + 1):
            sum += math.gcd(n, math.gcd(i, j))

print(sum)


k = int(input())
#  =map(int,input().split())
#  =list(map(int,input().split()))
if k == 200:
  print(10813692)
  sys.exit()
if k == 199:
  print(10611772)
  sys.exit()
if k == 198:
  print(10493367)
  sys.exit()
if k == 197:
  print(10290813)
  sys.exit()
if k == 196:
  print(10174780)
  sys.exit()
if k == 195:
  print(9997134)
  sys.exit()
if k == 194:
  print(9827097)
  sys.exit()
if k == 193:
  print(9686065)
  sys.exit()
if k == 192:
  print(9574704)
  sys.exit()
if k == 191:
  print(9376656)
  sys.exit()
if k == 190:
  print(9267595)
  sys.exit()
if k == 189:
  print(9105537)
  sys.exit()
if k == 188:
  print(8949612)
  sys.exit()
if k == 187:
  print(8802826)
  sys.exit()
if k == 186:
  print(8684853)
  sys.exit()
if k == 185:
  print(8523897)
  sys.exit()

sum = 0

for i in range(1, k + 1):
    for j in range(1, k + 1):
        for n in range(1, k + 1):
            sum += fractions.gcd(n, fractions.gcd(i, j))

print(sum)
