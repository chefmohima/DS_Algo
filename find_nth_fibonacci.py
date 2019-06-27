# find nth fibonacci number

# with memoization
def fibo(n,cache):
    if n <= 2:
        return 1
    else: 
        if n in cache:
            return cache[n]
        else:
            result = fibo(n-1,cache)+fibo(n-2,cache)
            cache[n] = result
            return result
			
			
# without memoization           
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        

c = {}        
fibo(6,c)
#fib(6)

