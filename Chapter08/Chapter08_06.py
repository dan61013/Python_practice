# 多型 (polymorphism)

class Animal():
    def __init__(self, name) -> None:
        self.name = name
    def who(self):
        return self.name
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__('小狗'+name)
    def sound(self):
        return '汪汪叫'

class Bird():
    def __init__(self, name) -> None:
        self.name = '小鳥'+name
    def who(self):
        return self.name
    def sound(self):
        return '啾啾叫'
    
def talk(obj):
    print(f'{obj.who()}正在{obj.sound()}')
    
def main():
    
    a = Animal('動物')
    talk(a)
    
    d = Dog('小黑')
    talk(d)
    
    b = Bird('小黃')
    talk(b)
    
if __name__ == '__main__':
    main()