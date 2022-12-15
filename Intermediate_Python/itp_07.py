# https://eastlakeside.gitbook.io/interpy-zh/set_data_structure
# set

def set_for_test_01():
    """原始做法"""
    alphabet_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    # print(alpha_list.count('a')) # 1
    
    duplicates = []
    for value in alphabet_list:
        if alphabet_list.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)
    print(duplicates)

def set_test_01():
    """優化做法"""
    alphabet_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    duplicates = set([x for x in alphabet_list if alphabet_list.count(x) > 1])
    print(duplicates)

def test_002():
    valid = set(['Dan', 'Ben', 'Ken', 'Mindy', 'Mira'])
    input_set = set(['Dan', 'Ken', 'Brian'])
    print("這是交集:", input_set.intersection(valid))
    print("這是差集:", input_set.difference(valid))

def main():
    set_for_test_01()
    set_test_01()
    test_002()
    
if __name__ == "__main__":
    main()