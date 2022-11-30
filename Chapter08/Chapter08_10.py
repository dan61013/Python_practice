# 類別方法 class method

class Animal():
    count = 0 # 沒有加上self, 是類別變數(class variable)
    
    def __init__(self) -> None:
        Animal.count += 1
    
    def kill(self):
        Animal.count -= 1
    
    @classmethod
    def show_count(cls): # 必要參數: cls
        print(f"現在有{cls.count}隻動物") # cls.variable_name 此方法可以呼叫類別變數

def main():
    
    a = Animal()
    Animal.show_count()
    
    b = Animal()
    Animal.show_count()
    
    c = Animal()
    Animal.show_count()
    
    a.kill()
    Animal.show_count()

if __name__ == '__main__':
    main()