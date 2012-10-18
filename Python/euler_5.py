# Euler 5
# Smallest number divisible by everything from 1..20

from euler_3 import smallest_divider

def main():
	numbers = xrange(2, 20)
	primes_list = []
	dicts =[] 
	for i, n in enumerate(numbers):
		primes_list.append(smallest_divider(n,n))
		dict = {}
		for elem in primes_list[i]:
			if elem in dict:
				dict[elem] += 1
			else:
				dict[elem] = 1
		dicts.append(dict)
	final = {}
	for dict in dicts:
		for key in dict:
			if key in final and final[key] < dict[key]:
				final[key] = dict[key]
			elif key not in final:
				final[key] = dict[key]


	product = 1
	for key in final:
		for i in xrange(0,final[key]):
			product *= final[key]

	print product






if __name__ == '__main__':
	main()