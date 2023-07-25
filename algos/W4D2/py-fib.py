from functools import lru_cache
# LRU Least Recently Used Cache

@lru_cache
def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)

for n in range(1, 510):
    print(fib(n))