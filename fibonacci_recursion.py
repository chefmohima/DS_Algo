# without memoization : O(N*N)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibo(n-1) + fibo(n-2)
    

# with memoization : O(N)    
fibo_cache = {}
def fibom(n):
    if n in fibo_cache:
        return fibo_cache[n]
    if n==1 or n==2:
        value = 1
    elif n > 2:
        value =  fibom(n-1) + fibom(n-2)
        # save value in cache
        fibo_cache[n] = value
    return value
    
fibom(6)