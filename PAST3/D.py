n = int(input())
s = []
for i in range(5):
    kari = input()
    s.append(kari[1:])
digit = 0
ans = []
for i in range(n):
    if(s[0][digit:digit+4] == "###."):  # 02356789
        if (s[1][digit:digit + 4] == "#.#."):  # 089
            if(s[2][digit:digit+4] == "###."):
                if (s[3][digit:digit + 4] == "#.#."):  # 08
                    ans.append("8")
                else:
                    ans.append("9")
            else:
                ans.append("0")
        elif(s[1][digit:digit+4] == "..#."):  # 23567->237
            if (s[2][digit:digit + 4] == "###."):  # 23
                if (s[3][digit:digit + 4] == "#..."):  # 2
                    ans.append("2")
                else:
                    ans.append("3")
            else:
                ans.append("7")
        else:  # 56
            if (s[3][digit:digit + 4] == "#.#."):  # 6
                ans.append("6")
            else:
                ans.append("5")
    else:  # 14
        if (s[2][digit:digit + 4] == "###."):  # 4
            ans.append("4")
        else:
            ans.append("1")
    digit += 4

print((''.join(ans)))
