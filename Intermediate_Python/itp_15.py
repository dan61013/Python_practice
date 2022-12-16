# https://eastlakeside.gitbook.io/interpy-zh/mutation
# Mutation 對象變動

def sample_01():
    """當variable01貼到02上，只是多一個標籤的概念，實體都是指向同一個位址(ID)"""
    foo = ['Hi']
    print(foo) # ['Hi']
    
    # bar = foo
    bar = foo
    # 所以當bar改變，foo也會被改變
    bar += ['bye']
    print(foo) # ['Hi', 'bye']

def sample_02(num, target=[]):
    """當默認參數出現空list，則會繼承並繼續執行"""
    target.append(num)
    return target

def sample_03(num, target=None):
    # 如果沒有帶入list參數，則初始化target = []
    if target is None:
        target = []
    target.append(num)
    return target

def main():
    print(sample_02(1))
    print(sample_02(2))
    print(sample_02(3))
    
    print(sample_03(1))
    print(sample_03(2))
    print(sample_03(3))

if __name__ == "__main__":
    main()