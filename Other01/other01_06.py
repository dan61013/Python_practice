# https://chriskang028.medium.com/python-%E8%A3%A1%E7%9A%84-yield-%E8%AE%93%E4%BD%A0%E7%B0%A1%E5%96%AE-%E5%BF%AB%E9%80%9F%E7%9E%AD%E8%A7%A3-yield-%E7%9A%84%E6%A6%82%E5%BF%B5-f660521f3aa7
# yield延伸閱讀

def test_case01():
    # range是以生成式進行
    # xrange (python2x) 才是以class進行
    my_list = [x*x for x in range(1000000)]
    for i in my_list:
        print(i)

def foo():
    print("Strat:")
    while True:
        throw = yield 10
        print("throw: {}".format(throw))

def bar():
    """生成式可以迭代，用()，而不是[]"""
    my_list = (i*i for i in range(4))
    for i in my_list:
        print(i)

def main():
    # test_case01()
    
    # 實作1:
    g = foo()
    print(next(g))
    print("*"*20)
    print(next(g))
    
    # send
    h = foo()
    print(next(h))
    print("*"*20)
    print(h.send(1000))
    
    # Generator 生成式 (1line)
    bar()

if __name__ == "__main__":
    main()