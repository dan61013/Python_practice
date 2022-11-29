# 新增參數的覆寫函式

class Animal():
    def __init__(self, name) -> None:
        self.name = name
    def sound(self):
        pass
    
class Dog(Animal):
    def __init__(self, name, leg) -> None:
        super().__init__('小狗: ' + name)
        self.leg = leg
    def sound(self):
        return '汪汪叫'

def main():
    a = Animal('小白')
    d = Dog('小黑', 4)
    
    print(f"{d.name}有{d.leg}條腿")
    print(d.name, d.sound())
    
    print(a.name)
    print(a.sound())
    
if __name__ == '__main__':
    main()