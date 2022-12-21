# Python求質數
# https://gist.github.com/uranusjr/581ba170cc5a42bdd3ff56ede01994ae

from math import *

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True # 質數

def print_prime():
    """以一行的方式，輸出所有質數"""
    num = int(input('Enter a integer:\n'))
    
    for i in range(2, num + 1):
        i_is_prime = is_prime(i)
        if i_is_prime:
            print(i, end=' ')

def dispart(n):
    """分解某一數值，並列出所有因數"""
    if is_prime(n):
        print([1, n])
    else:
        print([i for i in range(1, n + 1) if n % i == 0])

def main():
    
    dispart(29)
    
if __name__ == "__main__":
    main()