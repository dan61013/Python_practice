# 組合 Composition

# 把Leg做成一個class，並給予init值
class Leg():
    def __init__(self, num, look) -> None:
        self.num = num
        self.look = look

# 把leg命名成一個變數，並設定函式，來操作leg的變數(init)
class Animal():
    def __init__(self, name, leg) -> None:
        self.__name = name
        self.leg = leg
    
    def show_name(self):
        return self.__name
    
    def show(self):
        print(f"{self.show_name()}有{self.leg.num}隻{self.leg.look}腿")

def main():
    
    leg = Leg(4, '短短的')
    
    a = Animal('小黑', leg)
    
    a.show()

if __name__ == '__main__':
    main()