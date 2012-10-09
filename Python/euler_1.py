#Euler Problem 1

def multi_gen(number=0,max=0):
	multiplier = 1
	result = 0
	while result < max:
		result = number * multiplier
		yield result
		multiplier += 1

count = sum(x for x in multi_gen(5,1000))
count += sum(x for x in multi_gen(3,1000))
print count