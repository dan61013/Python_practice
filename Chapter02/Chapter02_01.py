"""
Chapter02: 資料型別、變數與運算子
int, bool, float, False的數值
"""
def main():
    
    # 實整數為True
    print(bool(1)) # True
    
    # 整數數值沒有範圍(X)
    # -2147483648 through 2147483647
    print(int(10**100))
    
    # 如果int的數值是小數，則直接取整數位
    print(int(3.14)) # 3
    
    # 表示100是二進位，轉換成十進位變成4
    print(int('100',2)) # 4
    
    # float可以把任何數值轉換成帶有小數點的數值
    print(float(3))
    print(float('3.1415'))
    print(float('3.14'))
    
    # 字串是不可變的物件(objects)
    
    s = str('Python')
    # s[0] = 'Q' -> 此方式不能修改String，會報錯

def false_objects():
    
    # 列印出所有代表False objects
    
    false_list = [
        False, 0, 0.0, None, (), [], {}, ''
    ]
    
    for i in false_list:
        print(bool(i))

if __name__ == '__main__':
    main()