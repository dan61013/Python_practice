# https://eastlakeside.gitbook.io/interpy-zh/comprehensions
# Comprehension 推導式

# 列表推導式
def list_comprehension():
    # 從0~29取出能被3整除的數值
    # [i for i in Where if 條件]
    multiples = [i for i in range(30) if i % 3 == 0]
    print(multiples)
    
    # example list.append()
    squared = []
    for i in range(10):
        squared.append(i**2)
    print(squared)
        
    # 簡化上述範例
    squared = [i**2 for i in range(10)]
    print(squared)

# 字典推導式
def dict_comprehension():
    mcase = {'a':10, 'b':34, 'A':7, 'Z':3}
    # 大小寫英文字母合併計數
    mcase_frequency = {
        k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
        for k in mcase.keys()
    }
    print(mcase_frequency)
    
    # key, value互換
    dict_01 = {1:'Dan', 2:'Mira', 3:'Ken', 4:'Ben'}
    dict_01_transform = {i:j for j, i in dict_01.items()}
    print(dict_01_transform)

def set_comprehension():
    # set集合推導式
    squared = {x**2 for x in [1,1,2]}
    print(squared)

def main():
    # list_comprehension()
    # dict_comprehension()
    set_comprehension()
    
if __name__ == "__main__":
    main()