
s = input()
t = input()

s = ''.join(sorted(s))
t = ''.join(sorted(t, reverse=True))

if s< t:
	print('Yes')
else:
	print('No')
