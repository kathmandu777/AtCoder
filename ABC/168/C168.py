import math
import sys
import numpy
import decimal

a, b, h, m = map(int, input().split())

sita = abs((h / 12 * 360+m/60*30) - (m / 60 * 360))

if (sita > 180):
    sita = 360-sita

ans = numpy.sqrt((a * a) + (b * b) - (2 * a * b*math.cos(math.radians(sita))))
print(decimal.Decimal(ans))
