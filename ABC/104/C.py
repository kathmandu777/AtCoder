import math

q_sum, goal = map(int, input().split())
q = []
for i in range(q_sum):
    q.append([100*(i+1)]+list(map(int, input().split())))
# [[100,2,300],...] => 100点の問題が2問あり、全て解いたら300点もらえる

ans = 99999999999999999999
for i in range(2 ** q_sum):
    num = 0
    points_sum = 0
    used_q = [0]*q_sum
    for j in range(q_sum):
        if ((i >> j) & 1):
            points_sum += q[j][0] * q[j][1] + q[j][2]
            num += q[j][1]
            used_q[j] = 1

    try:
        non_used_q = [i for i, x in enumerate(used_q) if x == 0]
        max_non_used_q_point = (max(non_used_q) + 1) * 100
        limit_num = q[max(non_used_q)][1]
        use_num = math.ceil((goal - points_sum) / max_non_used_q_point)
        if (use_num >= 0 and use_num < limit_num):
            points_sum += use_num * max_non_used_q_point
            num += use_num
    except:
        pass

    if (points_sum >= goal):
        ans = min(ans, num)

print(ans)
