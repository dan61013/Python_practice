# Decorator 應用

from functools import wraps

def decorator_name(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return func(*args, **kwargs)
    return decorated
    
@decorator_name
def func_01():
    return ("Function is running")

# 日誌
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + "was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
    """Do some math."""
    return x + x

if __name__ == "__main__":
    
    can_run = True
    print(func_01())
    
    can_run = False
    print(func_01())
    
    result = addition_func(11)