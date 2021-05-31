s = input()

len_s = len(s)


ans = 0

for i in range(2 ** (len_s - 1)):
    tmp = int(s[-1])
    pre_digit = 1
    for j in range(len_s - 1):
        # print(tmp)
        if ((i >> j) & 1):  # bitが1だったら
            tmp += int(s[-(j + 2)])
            pre_digit = 1
        else:
            tmp += int(s[-(j + 2)]) * 10 ** pre_digit
            pre_digit += 1
    ans += tmp

print(ans)
