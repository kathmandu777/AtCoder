#from icecream import ic
import math
from decimal import Decimal

k = int(input())
s = input()
t = input()

s_li = []
t_li = []
for si in s[0:4]:
    s_li.append(int(si))
for ti in t[0:4]:
    t_li.append(int(ti))

ans_li = []
for s in range(1, 10):
    for t in range(1, 10):
        s_li.append(s)
        t_li.append(t)
        #ic(s_li, t_li)
        s_score = 0
        t_score = 0
        for i in range(1, 10):
            if (s_li + t_li).count(i) > k:
                #ic((s_li + t_li).count(i))
                s_score = 0
                t_score = 0
                break
            s_score += i * (10 ** (s_li.count(i)))
            t_score += i * (10 ** (t_li.count(i)))
        if (s_score > t_score):
            ans_li.append([s, t])
        #ic(s_score, t_score)
        s_li.pop()
        t_li.pop()

# print(ans_li)
# print(len(ans_li))


def permutations_count(n, r):
    ans = 1
    for i in range(r):
        ans *= (n - i)
    return ans


ans_num = 0
card = [0] * 10
for i in range(1, 10):
    card[i] = k - (s_li + t_li).count(i)
for ans in ans_li:
    if ans[0] == ans[1]:
        ans_num += card[ans[0]] * (card[ans[1]] - 1)
    else:
        ans_num += card[ans[0]] * card[ans[1]]

print(min(1.00000000, Decimal(str(ans_num)) /
          Decimal(str(permutations_count(9 * k - 8, 2)))))
