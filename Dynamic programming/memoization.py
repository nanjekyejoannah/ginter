import functools

def fibn(n):
	memo = []
	if memo[n] != null:
		return memo[n]
	elif n == 1 or n == 2:
		return 1
	else:
		return fibn(n-1) + fib(n-2)
		memo[n] = fibn[n]

@functools.lru_cache(maxsize=128)
def fib(n):
	if n==0 or n== 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

fib.cache_info()
fib.clear_cache()