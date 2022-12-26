# https://eastlakeside.gitbook.io/interpy-zh/func_caching/python_32
# lru_cache
from functools import lru_cache, wraps

# Python 3.2+
@lru_cache(maxsize=32)
def fib(n: int)-> int: 
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# 輸入多次input (測試)
def test_input():
    for i in range(3):
        i = input("請輸入: ")
    return i

# Python 2+ 緩存機制
def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

@memoize
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    print([fib(n) for n in range(25)])
    fib.cache_clear()
    # print(test_input())
    print(fibonacci(25))

if __name__ == "__main__":
    main()