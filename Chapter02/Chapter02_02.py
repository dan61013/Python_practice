"""
id, variant, 算術、邏輯、in & is運算子
"""

def main():
    
    # 出現NameError，代表變數未定義
    # 一個物件的id值在CPython直譯器裡就代表它在記憶體中的地址
    # identity -> id()代表的是一個物件的身分證號碼
    a = 1
    print(a, id(a))
    a = 'python'
    print(a, id(a))
    
    x = 1
    y = x
    print(id(x), id(y))
    print(x, y)
    
    # 算術運算子
    a = (1+10*4)*(3-1)
    print(a) # 82
    
    # 邏輯運算子
    a = True
    b = False
    print(a and b)
    print(a or b)
    
    # in, is 運算子
    a = 1
    b = [1,2,3]
    print(a in b)

if __name__ == '__main__':
    main()