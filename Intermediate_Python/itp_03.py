"""
Generators生成器 (占用較少資源)
迭代器(iterators)，讓程序員可以遍歷一個容器(特別是list)的對象
迭代器並不會執行一個迭代
原因要了解以下三個部分:
1. 可迭代對象(Iterable)
2. 迭代器(Iterator): 只要定義了next(py2)或者__next__方法，就是一個迭代器
3. 迭代(Iteration): 從一個地方取出一個元素的過程，一個循環來遍歷某個東西時，就是迭代
python中，任一對象(object)，都定義了一個可以返回迭代器的__iter__方法，以及支持下標索引的__getitem__方法
"""

def generator_function():
    for i in range(20):
        yield i

# next()
def generator_function_02():
    for i in range(3):
        yield i
        
# Fibonacci
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def main():
    # 基本生成迴圈0~19
    # for item in generator_function():
    #     print(item)
    
    gen = generator_function_02()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    # print(next(gen)) # 這一行會產生Error: StopIteration
    
    # String不是一個iterator, 所以要先用iter才能使用next()函式
    txt = "Bboyworld"
    txt_iter = iter(txt)
    print(next(txt_iter)) # B
        
if __name__ == "__main__":
    main()