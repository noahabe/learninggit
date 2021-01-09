def f():
	print("this is the f() function")
	return 0

def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)

if __name__ == '__main__':
	f()

