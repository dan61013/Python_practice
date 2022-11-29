# class -> __eq__ 用法

class Animal():
    def __init__(self, name) -> None:
        self.__name = name
    def sound(self):
        pass
    def show_name(self):
        return self.__name
    def eq(self, __o):
        return self.__name == __o.show_name()
    def __eq__(self, __o: object) -> bool:
        return self.__name == __o.show_name()

class Dog(Animal):
    def __init__(self, name, leg: int) -> None:
        super().__init__('小狗'+name)
        self.leg = leg
    def sound(self):
        return '汪汪叫'

def main():
    
    d1 = Dog('小黑', 4)
    d2 = Dog('小黑', 4)
    print(d1.eq(d2))
    print(d1 == d2)

if __name__ == '__main__':
    main()