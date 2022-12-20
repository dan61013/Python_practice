# class

# Python3以後都是用新型態，但建議還是加上object比較好
class OldClass():
    def __init__(self) -> None:
        print('I am old class')

class NewClass(object):
    def __init__(self) -> None:
        print('I am a jazzy new class')

class GetTest(object):
    # instance被建立後會立即調用
    def __init__(self) -> None:
        print('Greetings!')
    def another_method(self):
        print('I am another method which is not automatically called')

class GetTest02(object):
    # instance被建立後會立即調用
    def __init__(self, name) -> None:
        print('Greetings!! {}'.format(name))
    def another_method(self):
        print('I am another method which is not automatically called')

class GetTest03(object):
    def __init__(self) -> None:
        self.info = {
            'name':'Dan',
            'country':'Taiwan',
            'number':'123765'
        }
        self.lst = ['Ben', 'Ken']
    # 允許class使用list[0] and dict['key']
    def __getitem__(self, i):
        return self.info[i], self.lst[0]

def main():
    old = OldClass()
    new = NewClass()
    
    a = GetTest()
    a.another_method()
    
    b = GetTest02('Dan')
    b.another_method()
    
    c = GetTest03()
    print(c['name']) # Dan
    print(c['country']) # Taiwan
    
if __name__ == "__main__":
    main()