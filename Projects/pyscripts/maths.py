import math
def root(n):
	return math.sqrt(n)

def sq(n):
	return math.pow(n,2)

def choose(n,k):
	num = math.factorial(n)
	den = math.factorial(k) * math.factorial(n-k)
	return num / den

def z(n,mu,sig):
	return (n - mu) / sig

def plusmin(x,y):
	a = x-y
	b = x+y
	return (a,b)
