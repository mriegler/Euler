# Euler 4

import itertools

def get_combinations(at, to):
	step = 10
	multiplied = (x for x in [])
	while at >= to:
		try:
			yield multiplied.next()
		except StopIteration:
			list = xrange(at, at-step, -1)
			print str(at)
			combinations = itertools.combinations(list,2)
			multiplied = (x * y for x, y in combinations)
			at -= step

for i, val in enumerate(get_combinations(999,100)):
	if str(val) == str(val)[::-1]:
		print str(val) + " i: " + str(i)
		break
