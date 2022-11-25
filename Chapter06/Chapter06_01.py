from datetime import datetime

def main():
    
    def hi():
        print('hi')
    hi()
    
    def min(a, b):
        if a > b:
            return b
        else:
            return a
        
    print(min(2, 4))
    
def area(x, y):
    return x * y

def f1():
    g = 10 # 區域變數，會被優先使用
    print(g)
    
def f(s: str, count=1):
    print(s * count)
    
def ymd():
    now = datetime.now()
    return (now.year, now.month, now.day)


if __name__ == '__main__':
    
    # main()
    
    f('hi')
    
    y, m, d = ymd()
    print('{}/{}/{}'.format(y, m, d))
    
    # g = 5 # 全域變數
    # f1()
    # a = int(input('輸入長: '))
    # b = int(input('輸入寬: '))
    # ans = area(a, b)
    # print('長方形面積: {}'.format(ans))