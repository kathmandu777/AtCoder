import itertools
# from #icecream import #ic

n, k = map(int, input().split())
time = []
for i in range(n):
    time.append(list(map(int, input().split())))

delay_list = []
for pattern in list(itertools.permutations(range(n - 1))):
    # ic(pattern)
    delay = 0
    delay += time[0][pattern[0] + 1]
    # ic(delay)
    for i in range(1, len(pattern)):
        delay += time[pattern[i - 1] + 1][pattern[i] + 1]
        # ic(delay)
    delay += time[pattern[- 1] + 1][0]
    delay_list.append(delay)

print(delay_list.count(k))
