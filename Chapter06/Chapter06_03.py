def main():
    x = lambda a, b: a + b
    print(x(1, 2))
    

def ch6_6_6():
    
    def run(func, x, y):
        return func(x, y)
    k = run(lambda a, b: a + b, 10, 20)
    print(k)

def irange(start: int, stop: int, step=1):
    if start < stop:
        i = start
        while i < stop:
            yield i
            i += step
    
    else:
        i = start
        while i > stop:
            yield i
            i += step
            
def func01():
    
    for i in range(1, 10):
        yield i*i

def hello(msg: str):
    def say(text: str):
        return 'Hello,' + text
    print(say(msg))
    print(say('你好'))
    
def hello_02(msg):
    def say(hi):
        return hi+msg
    return say

if __name__ == '__main__':
    # main()
    # ch6_6_6()
    hello('Dan')
    x = hello_02('hi')
    print(x('Dan'))
    # test_list = []
    # for test in func01():
    #     test_list.append(test)
    # print(test_list)
    # x = irange(1, 10)
    # print(x) # yield回傳的資料會被認為是產生器，要用for取出
    # for i in irange(1, 5, 1):
    #     print(i)