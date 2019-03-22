'''

Find fibonacci sequence using recursion {lru_cache } 

'''
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    
    #check if input is integer
    if type(n) != int:
        raise TypeError("Value must be integer")
    #check if Value is positive
    if n < 1:
        raise ValueError("Value must be positive integer")
    if n ==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,1000):
    print(n, ":", fibonacci(n))
    
