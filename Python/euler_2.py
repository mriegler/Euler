/*Project Euler Problem 2
*Copyright Marcel Riegler
*GPL Licensed
*/
def fib_gen(max = 0):
	"""Generates Fibonacci numbers upto max"""
	a, b = 0, 1
	while b < max:
		a, b = b, a + b
		yield a

count = sum(x for x in fib_gen(4000000) if (x%2) == 0)
print count