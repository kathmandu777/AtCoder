n = int(input())
norigin = n
alpha = ["", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ans26 = n//26
mod26 = n % 26
digit = [26, 676, 17576, 456976, 11881376, 308915776,
         8031810176, 208827064576, 5429503678976, 141167095653376]
ans = []

digitnum = 0
while True:
    digitnum += 1
    if (n - digit[digitnum - 1] <= 0):
        break
    else:
        n = n - digit[digitnum - 1]

for i in range(digitnum):
    ans.append(alpha[n % 26])
    n = n - (26 * (n//26))
print(''.join(ans))
"""

def digitcheck(ans26):
    i = 0
    while True:
        if (ans26 - digit[i] < 0):
            break
        else:
            ans26 = ans26 - digit[i]
            i += 1
    return alpha[ans26], norigin-digit[i]


digitnum = 0
while True:
    digitnum += 1
    if (n - digit[digitnum - 1] <= 0):
        break
    else:
        n = n - digit[digitnum - 1]

ans = []
for i in range(digitnum):
    anschild, ans26 = digitcheck(ans26)
    norigin = ans26
    ans26 = ans26//26
    ans.append(anschild)
    print(ans)
if(ans[-1]=="")
ans[-1] = alpha[mod26]
print(ans)
print(''.join(ans))
"""
