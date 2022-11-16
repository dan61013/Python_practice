"""
dict
"""

def main():
    
    # 取value, by key
    dict01 = {'今天':'today', '貓':'cat', '兔子':'rabbit'}
    print(dict01['貓'])
    
    # dict.get(key, '找不到回傳的話，回傳值該值')
    dict01 = {'今天':'today', '貓':'cat', '兔子':'rabbit'}
    print(dict01.get('今天'), dict01.get('狗'), dict01.get('飛機', '找不到該值'))

    # dict[key] = value -> 修改該鍵的值，若無，新增鍵值
    dict01 = {'今天':'today', '貓':'cat', '兔子':'rabbit'}
    dict01['今天'] = 'this day'
    print(dict01)
    dict01['狗'] = 'dog'
    print(dict01)
    # del dict[key] -> 刪除鍵值
    del dict01['今天']
    print(dict01)
    # clear 字典
    dict01.clear()
    print(dict01)
    
    # dict 可以把list or tuple，轉成dict (包含list(list)或各種組合)
    # a = dict(['早上', 'morning', '下午', 'afternoon']) # Error, 不能處理單層結構的list
    b = dict([['早上', 'morning'], ['下午', 'afternoon']])
    c = dict([('早上', 'morning'), ['下午', 'afternoon']])
    print(f'{b}\n{c}')
    
    # dict.copy() -> 複製dict，如果用"="，這樣在修改其中一方的字典時，另一邊也會被影響
    dict01 = {'a':0, 'b':1}
    dict02 = dict01.copy()
    dict02['c'] = 3
    print(dict01, dict02)

    # for 讀取字典的元素，要使用 for a, b in dict.items()
    dict01 = {'a':0, 'b':1}
    for key, value in dict01.items():
        print(f'key:{key}, value:{value}')
    
if __name__ == '__main__':
    main()