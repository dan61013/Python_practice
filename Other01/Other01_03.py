# collections Counter

from collections import Counter

def test_01():
    # Counter(string)
    a = 'BattleOfTheYears2022'
    counter = Counter(a)
    print(counter, type(counter))
    print(counter.most_common(3), type(counter.most_common(3))) # 輸出最常出現的3個元素
    print(counter.most_common(3)[1], type(counter.most_common(3)[1]))
    print(counter['t'])
    print(counter['Z']) # 不存在的值，回傳0
    
    counter.update('BboyKill')
    print(counter)

def test_02():
    # Counter(list or dict)
    counter = Counter(['a','a','k'])
    print(counter)
    counter = Counter({'a':2, 'k':1})
    print(counter)
    counter = Counter(a=2, k=1)
    print(counter) # 以上三個數值列印出來都是一樣的

def main():
    test_02()

if __name__ == "__main__":
    main()