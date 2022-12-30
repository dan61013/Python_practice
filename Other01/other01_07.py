# https://www.learncodewithmike.com/2020/01/python-method.html
# classmethod and staticmethod

# Instance Method 實例方式
class CarsA(object):
    # Instance Method
    def drive(self):
        print("Drive is instance method.")

class CarsB(object):
    # 建構式 Constructor
    def __init__(self):
        self.color = "Blue"
    
    # Instance method
    def drive(self):
        # self -> <__main__.CarsB object at 0x000001D441855100>
        print(f"{self} is {self.color}.")
        self.message()
    
    # Instance method
    def message(self):
        print("Message method is called.")

# 類屬性 class attribute
class CarsC(object):
    # class attribute
    door = 4
    
    def drive(self):
        self.__class__.door = 5

# 類方法 class method
class CarsD(object):
    # Class Method
    @classmethod
    def open_door(cls):
        print("Open door is class method")

# classmethod 只有cls(指向類)，所以無法改變object的狀態，因為缺少self
class CarsE(object):
    door = 4
    
    @classmethod
    def open_door(cls):
        print(f"{cls} has {cls.door} doors.")

# class method 常用於產生物件 Object
# 也稱為工廠方法 factory method
class CarsF(object):
    # Constructor
    def __init__(self, seat, color) -> None:
        self.seat = seat
        self.color = color
    # 箱型車
    @classmethod
    def van(cls):
        return cls(6, "black")
    # 跑車
    @classmethod
    def sports_car(cls):
        return cls(4, "yellow")

# Static Method Sample
class CarsG(object):
    # static method
    @staticmethod
    def accelerate():
        print("Accelerate is static method.")

# Static Method 實例
class CarsH(object):
    # 速率靜態方法
    @staticmethod
    def speed_rate(distance: int, min: int):
        return distance / min

if __name__ == "__main__":
    mazda = CarsB()
    mazda.drive()
    
    # 用__class__改變class attribute
    print(f"Cars origin door: {CarsC.door}")
    nissan = CarsC()
    nissan.drive()
    print(f"Cars new door: {CarsC.door}")
    
    # class method
    CarsD().open_door()
    
    # classmethod 無法改變object狀態
    toyota = CarsE()
    toyota.open_door()
    
    CarsE.open_door()
    
    # classmethod 建立物件 Object
    van = CarsF.van()
    sports_car = CarsF.sports_car()
    print(van.seat, van.color)
    print(sports_car.seat, sports_car.color)
    
    # static method 速率
    van = CarsH()
    van_rate = van.speed_rate(10000, 200)
    print(f"van rate: {van_rate:.2f}")
    
    # 通過類呼叫
    sports_car_rate = CarsH().speed_rate(20000, 20)
    print(f"sports car rate: {sports_car_rate:.2f}")