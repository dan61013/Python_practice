# collections (內建模組)
from collections import defaultdict


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
    print(counter_dict_01)
    
    # 建立一對多的multidict
    key_values = [('even',2),('odd',1),('even',8),('odd',3),('float',2.4),('odd',7)]
    multi_dict = {}
    for key, value in key_values:
        if key not in multi_dict:
            multi_dict[key] = value
        else:
            multi_dict[key].append(value)
    print(multi_dict)
    
def main():
    
    test_001()


if __name__ == "__main__":
    main()