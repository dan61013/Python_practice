# https://eastlakeside.gitbook.io/interpy-zh/decorators/everything_is_object
# Decorator(前置學習)

# 在函數中定義函數
def hi(name='isagi'):
    print("Now you are inside the hi() function")
    
    def greet():
        return "Now you are in the greet() function"
    
    def welcome():
        return "Now you are in the welcome() function"
    
    print(greet())
    print(welcome())
    print("Now you are back in the hi() function")

def new_hi(name='isagi'):
    def greet():
        return "Now you are in the greet() function"
    
    def welcome():
        return "Now you are in the welcome() function"
    
    if name == "isagi":
        return greet
    else:
        return welcome

def hi_02():
    return "Hi isagi"

def doSomethingBeforeHi(func):
    print("I am doing some boring work befor executing hi_02()")
    print(func())

def main():
    hi()
    # greet() # Name Defined Error
    a = new_hi()
    # print外層function只會顯示位置，因為最外層沒有其他物件，且if判斷是返還的是內部function
    print(a) # <function new_hi.<locals>.greet at 0x0000024DA3518CA0>
    # a() == new_hi()()，調用內層函數，且if name等於True，所以會print出greet
    print(a()) # Now you are in the greet() function
    
    # 先執行自己的第一行指令output01，然後再執行第二行，列印func() = hi_02()
    doSomethingBeforeHi(hi_02)
    # I am doing some boring work befor executing hi_02() -> output01
    # Hi isagi -> output02

if __name__ == "__main__":
    main()