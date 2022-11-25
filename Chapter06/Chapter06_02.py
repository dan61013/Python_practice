def main():
    pass

def func1(*args):
    # positional arguments
    print('位置引數為: ', args)
    print('1st: {}'.format(args[2]))
    
def func2(**kwargs):
    # keyword arguments
    print('關鍵字引數為: ', kwargs)
    
def func3(start: int, *args, **kwargs):
    print('start{}'.format(start))
    print('位置引數: {}'.format(args))
    print('關鍵字引數: {}'.format(kwargs))

def func4(g, length):
    """可以計算GSM的方式，
    輸入變數g=碼重(g/y), length=幅寬(inch)"""
    
    gsm = (g/length)*43
    return gsm

if __name__ == '__main__':
    main()
    
    func1(1, 2, 3)
    
    func2(a=1, b='Dan')
    
    func3(10, 1, 5, 'Dan', x=56, y=57, z='Max')
    
    help(func4)
    
    print(func4.__doc__)