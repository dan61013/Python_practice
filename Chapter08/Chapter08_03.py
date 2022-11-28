# 覆寫函式

class Animal():
    
    def __init__(self, name): # 不要把sound放入init屬性內
        self.name = name
    
    def sound(self):
        pass

class Dog(Animal):
    
    def __init__(self, name):
        super().__init__('小狗: ' + name)
    
    def sound(self): # 覆寫sound函式
        return '汪汪叫'

def main():
    
    d = Dog('小白')
    print(d.name)
    print(d.sound())
    
if __name__ == '__main__':
    main()