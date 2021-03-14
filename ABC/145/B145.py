import sys

n=int(input())
s=input()


if n%2==0 :
    for i in range(int(n/2)):
        if(s[i] != s[i+int(n/2)]):
            print('No')
            sys.exit()
    print('Yes')
else:
    print('No')
