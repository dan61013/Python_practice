def main():
    pass

def debug(func1):
    def func2(*args, **kwargs):
        print('正在執行函式:', func1.__name__)
        print('函式的說明文件:', func1.__doc__)
        print('位置引數:', args)
        print('關鍵引數:', kwargs)
        return func1(*args, **kwargs)
    return func2


# def add(a, b): # 這是一般的function用法
#     """回傳a+b的結果"""
#     return a + b

@debug
def add(a, b, c):
    """回傳a+b的結果"""
    return a + b + c

if __name__ == '__main__':
    main()
    
    # add = debug(add)
    # print(add(1, b=2))
    print(add(1, 2, c=3))