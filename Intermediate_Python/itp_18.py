# https://eastlakeside.gitbook.io/interpy-zh/collections
# deque, namedtuple

from collections import deque, namedtuple

# deque
def test_01():
    """使用方式類似list操作"""
    d = deque()
    print(type(d), type(deque))
    
    d.append('1')
    d.append(2)
    d.append('33')
    
    print(len(d), d, d[0])
    
    d_02 = deque(range(5))
    print(len(d_02))
    print(d_02.popleft()) # delete from left [0]
    print(d_02.pop()) # delete from right [-1]
    print(d_02)

def test_02():
    
    # 設定maxlen, 多出的參數，會從0開始被排除
    d = deque(range(30), maxlen=15)
    # deque([15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], maxlen=15)
    print(d)
    
    # extendleft, extend，從左&右邊拓展
    d_02 = deque([1, 2, 3, 4, 5])
    d_02.extendleft([0, 1])
    d_02.extend([10, 100, 101, 1001])
    print(d_02)

def test_03():
    """namedtuple是把tuple變成一個針對簡單任務使用的容器，
可以像字典一樣使用，是immutable"""
    Animal = namedtuple('Animal', 'name age type')
    cat_01 =  Animal('小黑', 1, 'cat')
    print(cat_01.name, cat_01.type)

# 在function內計算，並用namedtuple回傳對應的變數
def cal_01(a, b):
    sum = a + b
    multiply = a * b
    calculate = namedtuple('calculate', 'sum multiply')
    ans = calculate(sum, multiply)
    return ans

# named tuple 轉換成dictionary
def test_04():
    Animal = namedtuple('Animal', 'name age type')
    mira = Animal(name='Mira', age=1, type='cat')
    mira_dict = mira._asdict()
    print(mira_dict, type(mira_dict))

def main():
    # deque
    # test_01()
    # test_02()
    
    # namedtuple
    test_03()
    
    # namedtuple with function return
    calculate = cal_01(3, 5)
    print(calculate) # calculate(sum=8, multiply=15)
    
    # print namedtuple by dict
    test_04() # {'name': 'Mira', 'age': 1, 'type': 'cat'} <class 'dict'>
    
if __name__ == "__main__":
    main()