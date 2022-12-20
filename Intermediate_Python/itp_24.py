# https://eastlakeside.gitbook.io/interpy-zh/classes
# class
import math

class Cal(object):
    # pi是類變亮(通用)
    pi = math.pi
    
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self):
        return self.pi * (self.radius**2)

class SuperClass(object):
    superpowers = []
    
    def __init__(self, name) -> None:
        self.name = name
    
    def add_superpower(self, power):
        self.superpowers.append(power)

def main():
    a = Cal(32)
    print(a.area())
    print(a.pi)
    a.pi = 43
    print(a.pi)
    
    b = Cal(44)
    print(a.area())
    print(b.pi)
    b.pi = 50
    print(b.pi)
    
    dan = SuperClass('Dan')
    ben = SuperClass('Ben')
    # 實例變量(不會互相影響)
    print(dan.name)
    print(ben.name)
    # 類變量(通用)
    dan.add_superpower('fly')
    print(ben.superpowers) # ['fly']
    print(dan.superpowers) # ['fly']

if __name__ == "__main__":
    main()