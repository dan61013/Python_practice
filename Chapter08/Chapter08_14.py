# ch8\ex-1 形狀類別
import math

class Shape():
    
    def __init__(self, name) -> None:
        self.name = name
    
    def length(self):
        pass
    
class Tri(Shape):
    
    def __init__(self, name, a: int, b: int, c: int) -> None:
        super().__init__(f'三角形: {name}')
        self.a = a
        self.b = b
        self.c = c
    
    def length(self):
        return self.a + self.b + self.c
    
    def area(self):
        s = self.length() / 2
        return math.sqrt(s * (s-self.a)*(s-self.b)*(s-self.c))

class Rec(Shape):
    
    def __init__(self, name, a, b) -> None:
        super().__init__(name)
        self.a = a
        self.b = b
    
    def length(self):
        return (self.a + self.b) * 2

class Cir(Shape):
    
    def __init__(self, name, r: float) -> None:
        super().__init__(name)
        self.r = r
    
    def length(self):
        return 2 * math.pi * self.r
    
def ch8_ex1():
    
    a = Shape('形狀')
    t = Tri('三角形', 3, 4, 5)
    r = Rec('長方形', 4, 5)
    c = Cir('圓形', 5)
    
    print(a.name)
    print(f'{t.name}周長為{t.length()}')
    print(f'{r.name}周長為{r.length()}')
    print(f'{c.name}周長為{c.length():.2f}')

if __name__ == '__main__':
    ch8_ex1()