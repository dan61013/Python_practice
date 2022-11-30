# ch8/ex-5 自訂例外類別

class NegativeException(Exception):
    def __init__(self, index) -> None:
        super().__init__(self)
        self.index = index
    
try:
    
    a = [1, 2, 3, 4]
    
    index = int(input('輸入要存取的索引值: '))
    
    if index < 0:
        raise NegativeException(index)
    
    print(a[index])
    
except IndexError:
    print('索引值超出範圍')

except NegativeException as ne:
    print(f"輸入索引值為: {ne.index} ，索引值為負數")