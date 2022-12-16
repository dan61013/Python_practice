# https://eastlakeside.gitbook.io/interpy-zh/slots_magic
# slots魔法，python class __slots__
import time

# 不使用__slots__
class MyClassWithoutSlots(object):
    def __init__(self, name, birthday) -> None:
        self.name = name
        self.birthday = birthday
        
class MyClassWithSlots(object):
    __slots__ = ['name', 'birthday']
    def __init__(self, name, birthday) -> None:
        self.name = name
        self.birthday = birthday
        
def main():
    start01 = time.time()
    a = MyClassWithoutSlots('Dan', '0807')
    print(a.name, a.birthday)
    end01 = time.time()
    print(f"執行時間: {end01 - start01:.15f}秒")
    
    start02 = time.time()
    b = MyClassWithSlots('Ben', '0113')
    print(b.name, b.birthday)
    end02 = time.time()
    print(f"執行時間: {end02 - start02:.15f}秒")

if __name__ == "__main__":
    main()