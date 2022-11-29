# 新增函式

class Animal():
    def __init__(self, name) -> None:
        self.name = name
    def sound(self):
        pass
    
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__('小狗' + name)
    def sound(self):
        return '汪汪叫'
    def move(self):
        print(self.name + ' 在地上行走')
    
def main():
    d = Dog('小黑')
    print(d.name, d.sound())
    d.move()

if __name__ == '__main__':
    main()