# https://eastlakeside.gitbook.io/interpy-zh/lambdas
# lambda
import numpy as np
from pprint import pprint
import itertools

def test_01():
    a, b = 10, 2
    return a*b, a/b

def it_help():
    # https://ithelp.ithome.com.tw/questions/10211392
    # label = np.empty((17, 2), dtype=object)
    label = np.full((17, 2), fill_value="", dtype=object)
    label[1][1] = 'asd'
    label[2][1] = 'asd'
    print(str(label))

def test_02():
    my_dict = {'name':'Dan', 'habit':'Breaking', 'deposit':0}
    pprint(my_dict)

def test_03():
    lst = [['Dan', '1'], [5, 6], ['Ken', 7], [None, False]]
    print(list(itertools.chain.from_iterable(lst)))

class A(object):
    def __init__(self, a, b, c, d, e, f) -> None:
        # 直接用一行式同時更新多變數
        self.__dict__.update({k:v for k, v in locals().items() if k != 'self'})

class B(object):
    def __init__(self, name=str, age=int, habits=any) -> None:
        self.__dict__.update({k:v for k, v in locals().items() if k != 'self'})

class C(object):
    __slots__ = ['name', 'foundation']
    def __init__(self, name, foundation) -> None:
        self.name = name
        self.foundation = foundation
    
    def __str__(self):
        return f"BBoy: {self.name} will do {self.foundation}"

def main():
    add = lambda x,y: x + y
    print(add(3, 5))
    
    # 列表排序
    a = [(1, 2), (3, 4), (9, 10), (13, -3)]
    # 用x[1]，以tuple裡的[1]排序
    a.sort(key=lambda x: x[1])
    print(a, type(a[1]))
    
    # x, y = test_01()
    # print(x, y)
    
    # it_help()
    
    # pprint
    test_02()
    
    # itertools, 合併成一個單層list
    test_03()
    
    b = A(1, 2, 3, 4, 5, 6)
    print(b.__dict__)
    
    c = B('Dan', 27, 'Breaking')
    print(c.name)
    
    d = C('Dan', 'Windwill')
    print(d, d.name, d.foundation)
    # d.age = 27 # Error
    # print(d.age)
    print(d.__slots__)

if __name__ == "__main__":
    main()