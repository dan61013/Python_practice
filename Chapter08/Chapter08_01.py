class Animal():
    
    def __init__(self, name):
        self.name = name
        
class Dog(Animal):
    
    def __init__(self, name):
        
        # 使用super繼承
        super().__init__("小狗: {}".format(name))

def main():
    
    a = Animal('動物')
    b = Dog('小白')
    
    print(a.name)
    print(b.name)
    
if __name__ == '__main__':
    main()