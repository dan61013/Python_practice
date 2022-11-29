# 無法直接存取的變數

class Animal():
    def __init__(self, name) -> None:
        self.__name = name
    def sound(self):
        pass
    def show_name(self):
        return self.__name
    def __str__(self) -> str:
        return f'動物的隱藏名字為: {self.__name}'

class Dog(Animal):
    def __init__(self, name, leg) -> None:
        super().__init__('小狗' + name)
        self.leg = leg
    def sound(self):
        return '汪汪叫'

def main():
    d = Dog('小黑', 4)
    print(f'{d.show_name()}有{d.leg}條腿')
    print(d) # __str__方式

if __name__ == '__main__':
    main()