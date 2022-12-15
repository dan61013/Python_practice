# Decorator
from functools import wraps

def new_decorator_01(new_func_01):
    
    @wraps(new_func_01)
    def wrapTheFunction():
        print("I am doing some boring work before executing new_func_01()")
        
        new_func_01()
        
        print("I am doing some boring work after executing new_func_01()")
    
    return wrapTheFunction

def test_01():
    print("I am the function which needs some decoration to remove my foul smell")
    
@new_decorator_01
def test_02():
    """Hey you! Decorate me"""
    print("I am the function which needs some decoration to remove my foul smell")
    
def main():
    test_01()
    
    a = new_decorator_01(test_01)
    
    a()
    
    test_02()
    
    print(test_02.__name__) # wrapTheFunction, 如果沒有import wraps
    
if __name__ == "__main__":
    main()