# https://eastlakeside.gitbook.io/interpy-zh/collections
# enum.Enum

from collections import namedtuple
from enum import Enum

class Species(Enum):
    cat = 1
    dog = 2
    rabbit = 3
    dragon = 4
    raccoon = 5
    husky = 6
    fish = 7
    
    dan = 6
    mira = 1

def main():
    Animal = namedtuple('Animal', 'name age type')
    dan = Animal(name='Dan', age=27, type=Species.husky)
    mira = Animal(name='Mira', age=30, type=Species.cat)
    moon = Animal(name='Moon', age=1, type=Species.cat)
    
    # Species.type比較
    print(mira.type == moon.type) # True
    print(mira.type) # Species.cat
    
    # 枚舉取值
    print(Species(1))
    print(Species['cat'])
    print(Species.cat)
    
if __name__ == "__main__":
    main()