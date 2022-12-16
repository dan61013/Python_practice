# https://eastlakeside.gitbook.io/interpy-zh/collections
# collections, defauldict, counter

from collections import defaultdict, Counter
import collections, json

def test_01():
    
    habits = (
        ('Dan', 'Breaking'),
        ('Dan', 'Anime'),
        ('Mira', 'Anime'),
        ('Mira', 'Make up'),
        ('Ken', 'Reading')
    )
    
    habits_dict = defaultdict(list)

    for name, age in habits:
        habits_dict[name].append(age)
    print(habits_dict)

def test_02():
    some_dict = {}
    some_dict['name']['habits'] = 'Breaking' # KeyError

def test_02_solve():
    """import collections 解決 test_02的KeyError"""
    
    tree = lambda: collections.defaultdict(tree)
    some_dict = tree()
    
    some_dict['name']['habits'] = 'Breaking'
    print(json.dumps(some_dict)) # {"name": {"habits": "Breaking"}

def test_03():
    
    habits = (
        ('Dan', 'Breaking'),
        ('Dan', 'Anime'),
        ('Mira', 'Anime'),
        ('Mira', 'Make up'),
        ('Ken', 'Reading')
    )
    
    habits_counter = Counter(name for name, habit in habits)
    print(habits_counter)

def file_counter():
    # 統計文件
    with open('./Intermediate_Python/itp_01.py', 'rb') as f:
        line_count = Counter(f)
    print(line_count)

def main():
    test_01()
    # test_02()
    test_02_solve()
    
    # Counter
    test_03()
    
    # file count
    file_counter()
    
if __name__ == "__main__":
    main()