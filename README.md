# Python基礎

## 學習資源
參考資料: [Python程式設計: 從入門到進階應用](https://www.eslite.com/product/1001115182542678)

作者: 黃建庭 著 松崗數位文創股份有限公司

## Chapter00
### 安裝環境

Python(必要), 虛擬環境(Virtual Environment) 以及 Visual Studio Code(編輯介面，IDE)下載安裝

** IDE: Integrated Development Environment (集成開發環境)

1. [下載Python](https://www.python.org/downloads/)
2. [下載Anaconda](https://www.anaconda.com/)
3. [下載VScode](https://code.visualstudio.com/download)
---

## Chapter01
### Python的輸入及輸出

Python的輸入與輸出，主要有以下兩種功能

1. print(*object) -> 列印顯示出objects
```python
# 列印顯示出objects
print(*object)
```
2. Input([prompt]) -> 顯示[prompt]，讓使用者輸入文字(default: String)
```python
# 讓user輸入訊息
input([prompt])
```

---

## Chapter02
### 資料型別、變數與運算子

Python主要的資料型別有以下 種:

1. Bool (布林值)
2. Integer(整數)
3. Float(浮點數)
4. String(字串)

### False物件

1. False
2. 0
3. 0.0
4. None
5. () -> 空tuple
6. [] -> 空串列
7. {} -> 空字典
8. " -> 空字串

### 重點
    1. int範圍: -2147483648 through 2147483647
    2. String是不可變物件，不能直接用list取法去變更

### 變數

命名規則:

1. 第一個字為-> 英文大or小寫
2. 可以接[Unicode](https://zh.wikipedia.org/zh-tw/Unicode%E5%AD%97%E7%AC%A6%E5%B9%B3%E9%9D%A2%E6%98%A0%E5%B0%84), _ underline等符號
3. 不能用數字開頭
4. 可以用中文字
5. 大小寫英文視為不同

### 重點
變數 = 變數，則兩者的ID會相同

### 運算子

#### 指定運算子: =號右邊的數值先計算，再回傳給左邊的變數Variant

#### 算術運算子: +, -, *, /(浮點除法), //(整數除法), %(相除後求餘數), **(次方)

遞增: 在算術運算子的右邊，加上等於，就是遞增(減)算法

Example:
```python
a = a + 1
a += 1 # 答案同上列 a + 1
```

#### 比較運算子: <, <=, ==(等於), !=(不等於), >=, >

#### 邏輯運算子: and, or, not

#### in, is 運算子

#### 位元運算: &, |, ^, ~, <<, >>
分別是: 位元且運算, 位元或運算, 位元互斥或運算, 位元取相反, 位元左移運算, 位元右移運算

### 字串

String, 用'string'或"string"，都可以顯示字串

※不論是單引號或雙引號，都可以顯示包在裡面的引號

三引號，可以使用在多行文字(包括空白都會被列入範圍)

#### 字串運算子: +(合併str), *N(重複N次字串)

#### 切割字串

1. [:] -> 從開始到結尾
2. [5:] -> 從5到結尾
3. [-2:] -> 從-2到結尾
4. [:5] -> 從開始到5
5. [:-2] -> 從開始到-3
6. [7:9] ->從7~8
7. [-4:-1] -> 從-4~-2
8. [5:-2] -> 從5到-3
9. [::-1] -> 全部反轉
10. [-1::-1] -> 從-1到結尾，反轉
11. [2:10:2] -> 從2到9，間隔2

#### 串接多行 \\ -> 一行(換行編寫), \n ->換行, \t -> tab

### 彙整公式

    1. str.split(chars)
    2. chars.join(list)
    3. str.find(something)
    4. str.startswith(str)
    5. str.endswith(str)
    6. str.count(something)
    7. str.zfill(value)
    8. en: upper, lower, title, swapcase, capitalize

---

## Chapter03
### Python的資料儲存容器

### 儲存型態:

    1. tuple: 依序儲存，可照順序取出，不可變
    2. list: 依序儲存，可照順序取出，可變
    3. dict: Key:Value，無順序，可變
    4. set: 無順序
※ 暫存

---

## Chapter04
### 選擇結構

程式主要的3個結構:

    1. 循環結構: 依序執行
    2. 選擇結構: 條件測試
    3. 重複結構: 重複執行

主要功能有:
- if
- elif
- else

※ 補充:
1. if可以縮減成這樣的公式寫法:
```python
x = 1
print('Test' if x == 1 else 'False')
# True回傳的值 if 條件 else False回傳的值
# ans: Test
```

---

## Chapter05

### 迴圈與生成式

主要功能:
- for
- while

#### for while的基本組合應用

```python
# 最外層指定一個range迴圈
for i in range(2, 1000):
    # 並指定內層迴圈的起始值，以及判斷條件
    j = 2
    prime = True

    # 設定當內層迴圈j小於i的開根號=True
    while j < math.sqrt(i):
        if i % j == 0 # i除以J等於整除
            prime = False # 則不是質數
            break # 中斷處理
        j + 1
    
    if prime: # 如果當prime = True是質數
        print(i, '是質數') # 則列印出來

```

### break, continue, else

- break: 如果符合條件，就中斷，執行後面的程式碼
- continue: 如果符合條件，就跳過迴圈內之後的程式碼，重複執行到迴圈結束
- else: 如果迴圈正常結束，執行此程式

範例 (while, if, break, else):

```python

while True: # 無限迴圈
    num = int(input('輸入要猜的整數: '))

    if num == 100:
        print('你輸入的數值是100')
        break

    else:
        print('請再重猜，數值是1~100之間')

```

### for迴圈與資料儲存器
可以迭代的容器
1. tuple
2. list
3. dictionary
   
範例:
```python
# tuple
for i in range(tuple('index')):
    print(i) # i n d e x

lst = [1, 2, 3, 4, 5]
for i in range(0, len(lst)):
    print(i) # 1 2 3 ...

# 同時列印編號及元素
for i, element in enumerate(lst, start=1):
    print(i, element) # 1 1 ...

ch = ['台灣':'Taiwan', '車子':'car', '公開的':'public']

for key, value in ch.items():
    print(key, value) # 台灣 Taiwan ...

for key in ch.keys():
    print(key, ch[key]) # 台灣 Taiwan ...

for value in ch.values():
    print(value) # Taiwan car ...

```

### 生成式 Comprehension

```python
# 生成一般串列
[x for x in range(1, 6)]

# 按照判斷條件生成串列
[x for x in range(1, 11) if x % 2 == 1]

# 巢狀生成式
[(i, j, i * j) for i in range(1, 10) for j in range(1, 10)]

# dictionary生成式, 用計算字母出現次數舉例
word = 'bboyworld'
word_count = key : word.count(key) for key in set(word)
for w in word_count:
    print(w, word_count[w])
```
### 補充函數:

- python內建函數: chr() -> 返回一個整數值的ASCII字符
- python內建函數: ord() -> 返回一個值的十進制整數

---

## Chapter06

### 函式與遞迴

函式用於結構化程式，可以幫助多位程式設計師共同開發系統，
事先規劃好函式名稱與功能，再各自開發函式與整合所有程式，
最後達成系統所需功能。

### 函式的呼叫方法

1. function_name(v01, v02, ...) -> 無回傳值的呼叫方式
2. variable_01 = function_name(v01, v02, ...) -> 有回傳值的呼叫方式

```python
# function的區域、全域變數
g = 5
def t01():
    g = 10
    print(g) # 答案會是g=10，如果function內部沒有定義g，則g=5

# 預設變數
def t02(v01, v02=2):
    return v01 * v02

print(t02(3)) # 答案等於6

def t03(a, b, c):
    a += 2
    b += 3
    c += 4
    return (a, b, c)

x, y, z = t03(2, 3, 4)
print(x, y, z) # 答案等於(4, 6, 8)
```

### 位置引數(Positional arguments)

```python
# args裡面可以用','分隔輸入多個數值，會以tuple的方式呈現
def func_01(*args):
    print('位置引數為', args)
```

### 關鍵字引數(Keyword arguments)

```python
def func_02(**kwargs):
    print('關鍵字引數為', kwargs)
```
### 函式的說明文件

用三引號的方式，可以新增函式說明

```python
def func():
    """這理是
    function的說明內容"""
    return
# 顯示function說明內容的兩個方式
# 1. help
help(func)
# 2. __doc__
print(func.__doc__)
```

### 函式視為物件 (object)

python中，函數視為object，加上()括號才會執行該程式。

### 函式lambda

函式如果只有一行，可以轉換成函式lambda

```python
def add(a, b):
    return a + b
# lambda函數
lambda a, b: a + b

def t01(func, x, y):
    return func(x, y)
# 把lambda函數代入t01函式
k = t01(lambda: a, b: a + b, 10, 20)
print(k) # k = 30
```

### 函式產生器

```python
def irange(start: int, end: int, step=1):
    for i in range(start, end, step):
        yield i*i
x = irange(1, 10)

for i in x:
    print(i)
```

### 內部函式, closure函式

```python
# 內部函數
def func1():
    def func2():
        return
    # 執行func1的動作
# closure函式
def hello(msg):
    def say(hi):
        return hi+msg
    return say
x = hello('Dan')
print(x('Hi ')) # 結果: Hi Dan
```

### Decorator 裝飾器

```python
def debug(func1):
    def func2(*args, **kwargs):
        print('正在執行函式:', func1.__name__)
        print('函式的說明文件:', func1.__doc__)
        print('位置引數:', args)
        print('關鍵引數:', kwargs)
        return func1(*args, **kwargs)
    return func2

@debug
def add(a, b, c):
    '''計算a+b+c'''
    return a + b + c
```

### 遞迴 Recursion Function (遞迴函式)

```python
def recursive(a, b):

    if 條件判斷:
        return something
    else:
        return recursion_function
        # ex: recursive(參數a-1, 參數b+1)
```
## Chapter07

### 模組、套件與獨立程式

- 模組指的就是: 每一個python檔案
- 透過匯入其他python模組，就可以不斷地被其他程式再利用
- 單字: 變數、運算子等
- 句子: 多個變數、運算子、邏輯組合成一行程式
- 段落: 多行程式組合成函式
- 文章: 堆個函式組成模組

### 匯入模組的方式

```python
# 1
import sys
# 2
from sys import path
# 3
import sys as s
```

### 腳本程式

```python
if __name__ == '__main__:
    # doing something
```

---

## Chapter08

### 類別與例外

```python
class Animal():
    # __init__表示宣告類別時，會自動執行的函式
    def __init__(self, name): # 第一個參數預設是self，後面可以放其他參數
        self.name = name
a = Animal('動物')
print(a.name) # 動物
```

### 繼承

- 原有的類別，被稱為:
  
    1. 基礎類別: base class
    2. 雙親類別: parent class
- 新的類別，被稱為:
  
    1. 衍生類別: derived class
    2. 子類別: child class

使用derived class來定義類別間的繼承關係，
衍生類別就繼承了基礎類別，在衍生類別使用***super().基礎類別的函數***，可以呼叫基礎類別的函式來幫忙。