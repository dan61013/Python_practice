# https://eastlakeside.gitbook.io/interpy-zh/decorators/deco_with_args/deco_class
# 裝飾器類 Decorator class

# 用__call__方式來實現decorator
class logit(object):
    
    _logfile = './Intermediate_Python/out.log'
    
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        
        # 打開logfile
        with open(self._logfile, 'a') as opened_file:
            # 寫入log文字
            opened_file.write(log_string + '\n')
            
        self.notify()
        
        return self.func(*args, **kwargs)
    
    def notify(self):
        pass
    
class email_logit(logit):
    """一個logit的實現版本，可以在調用函數時，發送email給管理員"""
    
    def __init__(self, email = 'max912131@gmail.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)
        
    def notify(self):
        pass
    
def main():
    logit._logfile = './Intermediate_Python/out2.log'

    @logit
    def myfunc_01():
        pass

    myfunc_01()
    
if __name__ == "__main__":
    main()