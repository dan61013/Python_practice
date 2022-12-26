# https://eastlakeside.gitbook.io/interpy-zh/context_managers
# 上下文管理器
# 使用Decorator and Generators來實現
from contextlib import contextmanager

# 常見的with
def foo():
    with open('./Intermediate_Python/test_file.txt', 'w') as opened_file:
        opened_file.write('Hi Dan~')

class File(object):
    def __init__(self, file_name, method) -> None:
        self.file_obj = open(file_name, method)
    
    def __enter__(self):
        return self.file_obj
    
    def __exit__(self, type, value, traceback):
        # 新增Error處理方式
        print("Exception has been handled.")
        
        # 原先的__exit__是返回None
        self.file_obj.close()
        
        # 新增Error處理方式
        return True

def bar():
    """
1. with語句先暫存了File class的 __exit__方法
2. 然後再調用File class的 __enter__方法
3. __enter__ 方法打開文件並返回給with語句
4. 打開的文件句柄，被傳遞給opened_file參數
5. 我們使用.write()來寫入文件
6. with語句調用之前暫存的 __exit__方法
7. __exit__關閉了文件
    """
    with File('./Intermediate_Python/demo.txt', 'w') as opened_file:
        opened_file.write('Test by Dan!')

# 錯誤的方式
def foo_bar():
    with File('./Intermediate_Python/demo.txt', 'w') as opened_file:
        opened_file.undefined_function('Test Dan')

# Decorators and Generators 實現
@contextmanager
def open_file(name):
    """
1. 遇到了yield，所以建立一個生成式(而非普通函式)
2. @contextmanger，會被調用並傳入函數名(open_file)作為參數
3. contextmanager，函數返還一個以GeneratorContextManager對象封裝的生成器
4. 這個GeneratorContextManager被賦值給open_file函數，我們實際上是再調用GeneratorContextManager對象
    """
    f = open(name, 'w')
    yield f
    f.close()

def main():
    foo()
    bar()
    foo_bar()

if __name__ == "__main__":
    main()