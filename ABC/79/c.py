abcd = input()


for i in range(2 ** 3):
    tmp = int(abcd[0])
    op = []
    for j in range(3):
        # print(tmp)
        if ((i >> j) & 1):  # bitが1だったら
            tmp += int(abcd[j+1])
            op.append("+")
        else:
            tmp -= int(abcd[j+1])
            op.append("-")

    if (tmp == 7):
        for k in range(3):
            print(abcd[k], end="")
            print(op[k], end="")
        print(abcd[-1], end="")
        print("=7")
        break
