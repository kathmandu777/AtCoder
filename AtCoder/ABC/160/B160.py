import math


a=int(input())


fiveHun=math.floor(a/500)
five=math.floor((a-500*fiveHun)/5)

print(fiveHun*1000+five*5)











