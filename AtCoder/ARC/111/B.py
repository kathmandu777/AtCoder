import collections
import itertools
import sys

n = int(input())
color = [list(map(int, input().split())) for _ in range(n)]
flatten_color = list(itertools.chain.from_iterable(color))
c = collections.Counter(flatten_color)
color_count = c.most_common()[::-1]


ans = 0
for i in range(n):
    try:
        index = flatten_color.index(color_count[i][0])
    except ValueError:
        continue
    except IndexError:
        print(ans)
        sys.exit()

    if (index % 2 == 0):
        flatten_color[index:index + 2] = [-1, -1]
        ans += 1
    else:
        flatten_color[index - 1:index + 1] = [-1, -1]
        ans += 1
print(ans)
