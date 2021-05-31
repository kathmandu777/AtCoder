import sys
a, b, x = map(int, input().split())

if a>x:
  print("NO")
  sys.exit()
if b >= x - a:
    print("YES")
else:
    print("NO")