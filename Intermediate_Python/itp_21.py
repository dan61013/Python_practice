# https://eastlakeside.gitbook.io/interpy-zh/introspection/dir
# Introspection, 自省
# dir
# inspect
import inspect

def test_01():
    my_list = [1, 2, 3, 4]
    # dir -> 列出所有的屬性和方法, type=list
    print(dir(my_list))
    
    # type will return the class of object
    print(type(''))
    print(type([]))
    print(type({}))
    print(type(dict))
    print(type(3))
    
    # id, return the identity of object
    name = 'Dan'
    print(id(name))
    print(id('Dan'))
    
def test_02():
    # 獲取一個對象裡的所有member
    print(inspect.getmembers(str))
    
def main():
    # test_01()
    test_02()
    
if __name__ == "__main__":
    main()