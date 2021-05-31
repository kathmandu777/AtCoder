import sys


def forcheck(times):
    print("times", times)
    if (times == 5):
        sys.exit()
    times += 1
    for i in range(2):
        print("for", i)
        forcheck(times)


times = 1
forcheck(times)
