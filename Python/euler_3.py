# Euler 3
from math import sqrt

def smallest_divider(quotient, max_factor):
	factor = 2
	increment = 1
	while factor <= max_factor:
	 	if (quotient % factor) == 0:
	 	  	yield factor
	 	  	quotient /= factor
	 	else:
	 		factor += increment
	 		if factor == 3:
	 		  	increment = 2 # Skip the even ones after 2  


def main():
	for i in smallest_divider(600851475143,sqrt(600851475143)):
		print i

if __name__ == '__main__':
	main()