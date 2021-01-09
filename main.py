def f():
	print("this is the f() function")
	return 0

def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)

def fib_not_recursive(n):
	x = 0
	y = 1
	if n == 0:
		return x
	elif n == 1:
		return y
	while n-2 >= 0:
		x,y = y,x+y
		n -= 1 
	return y

if __name__ == '__main__':
	fib_generated_by_recurse = [fib(i) for i in range(0,20)]
	fib_generated_by_non_recurse = [fib_not_recursive(i) for i in range(0,20)]
	print(fib_generated_by_recurse)
	print(fib_generated_by_non_recurse)
