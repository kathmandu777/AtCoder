
s = input()
slen = len(s) - 1
sum = 0
for i in range(2 ** (slen)):
    oplist = [""]*(len(s)-1)
    for j in range(slen):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            oplist[len(s) - 2 - j] = "+"

    siki = ""
    for i in range(len(oplist)):
        siki += s[i] + oplist[i]
    siki += s[-1]
    sum += eval(siki)

print(sum)
