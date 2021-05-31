def main():
    from sys import stdin
    from collections import defaultdict
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        s = stdin.readline()[:-1]
        if d[s] == 0:
            d[s] += 1
            print(i + 1)


main()

# "something" in list は遅い
# dict["something"]は早い
