def main():
    n = int(input())
    ans = []
    for i in range(2**n):
        s = ""
        for j in range(n):
            if (i >> j) & 1:
                s += ")"
            else:
                s += "("
        # print(s)
        num_l = num_r = 0
        for j in range(n):
            if s[j] == "(":
                num_l += 1
            else:
                num_r += 1
            if not num_l >= num_r:
                break
        if j == n - 1 and num_r == num_l:
            ans.append(s)
    ans.sort()
    print("\n".join(ans))


main()
