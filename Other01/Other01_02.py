# collections (內建模組)
from collections import defaultdict

def zero(): # defaultdict, 當起始值為0的時候使用
    return 0

def test_001():
    # defaultdict
    
    # 統計list裡每一個元素出現的次數
    list01 = ['a','b','c','d','a','b']
    counter_dict_01 = {}
    for element in list01:
        if element not in counter_dict_01:
            counter_dict_01[element] = 1
        else:
            counter_dict_01[element] += 1
    print(f'統計list裡每一個元素出現次數:\n{counter_dict_01}')
    
    # 建立一對多的multidict
    key_values = [('even',2),('odd',1),('even',8),('odd',3),('float',2.4),('odd',7)]
    multi_dict = {}
    for key, value in key_values:
        if key not in multi_dict:
            multi_dict[key] = [value] # append list
        else:
            multi_dict[key].append(value)
    print(f'一對多的dict:\n{multi_dict}')
    
    # defaultdict
    better_dict = defaultdict(list) # default值以一個list()方式產生
    check_default = better_dict['a']
    print(check_default) # 輸出list方式產生的空串列[]
    
    better_dict['b'].append(1) # [1]
    better_dict['b'].append(2) # [1,2]
    better_dict['b'].append(3) # [1,2,3]
    print(f'測試default_dict: {better_dict["b"]}')

    # 改善後的一對多
    multi_dict = defaultdict(list)
    key_values = [('even',2),('odd',1),('even',8),('odd',3),('float',2.4),('odd',7)]
    
    for key, value in key_values:
        multi_dict[key].append(value)
        
    print(f'default_dict方式產生的一對多:\n{multi_dict}')
    
    # 不能給予defauldict一個固定的值，會產生typeError
    counter_dict_02 = defaultdict(zero)
    # counter_dict_02 = defaultdict(list) # int 不能迭代
    a_list = ['a','b','x','a','a','b','z']
    
    for element in a_list:
        counter_dict_02[element] += 1
    
    print(counter_dict_02)
    
    # default_factory: 第一個接受函數對象以後，都比照一般dict傳入格式
    # __missing__(key): 在我們調用不存在的key時，defaultdict會調用這個方法

def main():
    
    test_001()

if __name__ == "__main__":
    main()