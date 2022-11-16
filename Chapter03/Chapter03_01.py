"""
Python 儲存容器
tuple, list, dictionary, set
"""

def main():
    
    # tuple
    t1 = (1,2,3)
    t2 = 3, 2, 1
    print(t1, type(t1), t2, type(t2))
    
    # 取出tuple: unpacking (開箱)
    a, b, c = t1
    print(a, b, c) # 1 2 3
    
    # tuple 交換
    a, b = 15, 30
    print(a, b)
    a, b = b, a
    print(a, b)
    
    # list 轉tuple
    list_01 = [1, 2, 3, 4, 5]
    t01 = tuple(list_01)
    print(t01, type(t01))

    # 單一元素的tuple，要有"，"才會被判斷為tuple
    t01, t02 = ("z", ), ("a")
    print(type(t01), type(t02))
    
    # list
    bboy = ['windmill', 'flare', 'air flare']
    print(type(bboy))
    
    # [0]索引取值 (類似str切割字串操作)，len(list) -> 計算長度
    bboy = ['windmill', 'flare', 'air flare']
    print(bboy[0], len(bboy))
    
    # 修改元素
    bboy = ['windmill', 'flare', 'air flare']
    bboy[1] = 'elbow air flare'
    print(bboy)
    
    # index找出位置
    bboy = ['windmill', 'flare', 'air flare']
    print(bboy.index('flare'))
    
    # append -> 加到最後一個元素；insert -> 加到指定位置
    bboy = ['windmill', 'flare', 'air flare']
    bboy.append('elbow air flare')
    bboy.insert(2, 'ice')
    print(bboy)
    
    # remove -> 移除指定元素；del -> 刪除第N個元素
    bboy = ['windmill', 'flare', 'air flare']
    bboy.remove('flare')
    print(bboy)
    del bboy[0]
    print(bboy)
    
    # pop() -> 刪除最後一個元素
    bboy = ['windmill', 'flare', 'air flare']
    bboy.pop()
    print(bboy)
    
    # pop(0) -> 刪除第一個元素
    bboy = ['windmill', 'flare', 'air flare']
    bboy.pop(0)
    print(bboy)
    
    # sort() -> 排列元素
    a = ['j', 'a', 'z', 'b']
    a.sort()
    print(a)
    
    # for variant in list -> 可以讀取串列所有變數
    bboy = ['windmill', 'flare', 'air flare']
    for i in bboy:
        print(i)
        
    # 串接兩個list
    a = [1, 2, 3]
    b = ['apple', 'music', 'cat']
    print(a + b)
    
    # string 產生list
    print(list('object-oriented-programming'))
    
    # split 也會回傳list
    date_01 = '2022.01.15'
    a = date_01.split('.')
    print(a, type(a))

if __name__ == '__main__':
    main()