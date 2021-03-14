n = int(input())
li = []

sumac = 0
sumwa = 0
sumtle = 0
sumre = 0

for i in range(n):
    case = input()
    if (case == "AC"):
        sumac += 1
    elif (case == "WA"):
        sumwa += 1
    elif (case == "TLE"):
        sumtle += 1
    else:
        sumre += 1

print("AC x " + str(sumac))
print("WA x " + str(sumwa))
print("TLE x " + str(sumtle))
print("RE x "+str(sumre))
