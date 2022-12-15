# Decorato
# 在函數中嵌入裝飾器

from functools import wraps

# 產生函式被呼叫的log檔案
def logit(logfile = './Intermediate_Python/out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + "was_called"
            print(log_string)
            
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
                
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

@logit(logfile='./Intermediate_Python/func2.log')
def myfunc2():
    pass

if __name__ == "__main__":
    myfunc1()
    myfunc2()