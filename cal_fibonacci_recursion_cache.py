'''

Find fibonacci sequence using recursion {SUPER SLOW } 
Find fibonacci sequence using recursion {using cache } 
'''
fibonacci_cache = {}

def fibonacci_SLOW(n):
    if n ==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_SLOW(n-1) + fibonacci_SLOW(n-2)


def fibonacci_fast_cache(n):
    #if we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
        
    #Compute the Nth term
    if n ==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_fast_cache(n-1) + fibonacci_fast_cache(n-2)
       
    #cache the va;ue and return it
    fibonacci_cache[n] = value
    return value
    
for n in range(1,101):
    print(n, ":", fibonacci_fast_cache(n))
    
