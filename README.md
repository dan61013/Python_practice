# Python基礎

## 學習資源
參考資料: 
* [Python程式設計: 從入門到進階應用](https://www.eslite.com/product/1001115182542678)
* [Python进阶](https://eastlakeside.gitbook.io/interpy-zh/)
* [Python Type Hints](https://segmentfault.com/a/1190000040864758)
* [typing — Support for type hints](https://docs.python.org/3/library/typing.html)
---

## Table of contents
- [Python基礎](#python基礎)
  - [學習資源](#學習資源)
  - [Table of contents](#table-of-contents)
  - [Chapter00](#chapter00)
    - [0-1 安裝環境](#0-1-安裝環境)
  - [Chapter01](#chapter01)
    - [1-1 Python I/O](#1-1-python-io)
  - [Chapter02](#chapter02)
    - [2-1 資料型別、變數與運算子](#2-1-資料型別變數與運算子)
    - [2-2 False Objects](#2-2-false-objects)
    - [2-3 變數](#2-3-變數)
    - [2-4 運算子](#2-4-運算子)
      - [2-4-1 指定運算子](#2-4-1-指定運算子)
      - [2-4-2 算術運算子](#2-4-2-算術運算子)
      - [2-4-3 比較運算子](#2-4-3-比較運算子)
      - [2-4-4 邏輯運算子](#2-4-4-邏輯運算子)
      - [2-4-5 in, is 運算子](#2-4-5-in-is-運算子)
      - [2-4-6 位元運算](#2-4-6-位元運算)
    - [2-5 字串](#2-5-字串)
      - [2-5-1 字串運算子](#2-5-1-字串運算子)
      - [2-5-2 切割字串](#2-5-2-切割字串)
      - [2-5-3 串接多行](#2-5-3-串接多行)
    - [2-6 彙整公式](#2-6-彙整公式)
  - [Chapter03](#chapter03)
    - [3-1 Python的資料儲存容器](#3-1-python的資料儲存容器)
      - [3-1-1 儲存型態:](#3-1-1-儲存型態)
  - [Chapter04](#chapter04)
    - [4-1 選擇結構](#4-1-選擇結構)
  - [Chapter05](#chapter05)
    - [5-1 迴圈與生成式](#5-1-迴圈與生成式)
      - [5-1-1 for while的基本組合應用](#5-1-1-for-while的基本組合應用)
    - [5-2 break, continue, else](#5-2-break-continue-else)
    - [5-3 for迴圈與資料儲存器](#5-3-for迴圈與資料儲存器)
    - [5-4 生成式 Comprehension](#5-4-生成式-comprehension)
    - [5-5 補充函數:](#5-5-補充函數)
  - [Chapter06](#chapter06)
    - [6-1 函式與遞迴](#6-1-函式與遞迴)
    - [6-2 函式的呼叫方法](#6-2-函式的呼叫方法)
    - [6-3 位置引數(Positional arguments)](#6-3-位置引數positional-arguments)
    - [6-4 關鍵字引數(Keyword arguments)](#6-4-關鍵字引數keyword-arguments)
    - [6-5 函式的說明文件](#6-5-函式的說明文件)
    - [6-6 函式視為物件 (object)](#6-6-函式視為物件-object)
    - [6-7 函式lambda](#6-7-函式lambda)
    - [6-8 函式產生器](#6-8-函式產生器)
    - [6-9 內部函式, closure函式](#6-9-內部函式-closure函式)
    - [6-10 Decorator 裝飾器](#6-10-decorator-裝飾器)
    - [6-11 遞迴 Recursion Function (遞迴函式)](#6-11-遞迴-recursion-function-遞迴函式)
  - [Chapter07](#chapter07)
    - [7-1 模組、套件與獨立程式](#7-1-模組套件與獨立程式)
    - [7-2 匯入模組的方式](#7-2-匯入模組的方式)
    - [7-3 腳本程式](#7-3-腳本程式)
  - [Chapter08](#chapter08)
    - [8-1 類別與例外](#8-1-類別與例外)
    - [8-2 實例函數 (Instance class)](#8-2-實例函數-instance-class)
    - [8-3 繼承](#8-3-繼承)
    - [8-4 覆寫函式](#8-4-覆寫函式)
    - [8-5 類別方法 (classmethod)](#8-5-類別方法-classmethod)
    - [8-6 靜態方法 (staticmethod)](#8-6-靜態方法-staticmethod)
    - [8-7 Exception 例外](#8-7-exception-例外)
  - [Chapter09](#chapter09)
    - [9-1 進階字串處理](#9-1-進階字串處理)
    - [9-2 ASCII](#9-2-ascii)
    - [9-3 Unicode 編碼](#9-3-unicode-編碼)
    - [9-4 編碼 (encode)](#9-4-編碼-encode)
    - [9-5 解碼 (decode)](#9-5-解碼-decode)
    - [9-6 正規表示式 (regular expression)](#9-6-正規表示式-regular-expression)

---

## Chapter00
### 0-1 安裝環境

1. Python(必要)
2. 虛擬環境(Virtual Environment)
3. Visual Studio Code(編輯介面 IDE)

* IDE: Integrated Development Environment (集成開發環境)

1. [下載Python](https://www.python.org/downloads/)
2. [下載Anaconda](https://www.anaconda.com/)
3. [下載VScode](https://code.visualstudio.com/download)

---

## Chapter01
### 1-1 Python I/O

Python的輸入與輸出，主要有以下兩種功能

1. `print(*object)` -> 列印顯示出objects
```python
# 列印顯示出objects
print(*object)
```
2. `Input([prompt])` -> 顯示[prompt]，讓使用者輸入文字(default: String)
```python
# 讓user輸入訊息
input([prompt])
```
---
## Chapter02
### 2-1 資料型別、變數與運算子

Python主要的資料型別有以下4種:
1. Bool (布林值)
2. Integer (整數)
3. Float (浮點數)
4. String (字串)
### 2-2 False Objects
1. `False`
2. `0`
3. `0.0`
4. `None`
5. `()` -> 空tuple
6. `[]` -> 空串列
7. `{}` -> 空字典
8. `"` or `""` -> 空字串

重點整理
1. int範圍: `-2147483648` through `2147483647`
2. String是不可變物件，不能直接用list取法去變更

### 2-3 變數

命名規則:
1. 第一個字為-> 英文大or小寫
2. 可以接[Unicode](https://zh.wikipedia.org/zh-tw/Unicode%E5%AD%97%E7%AC%A6%E5%B9%B3%E9%9D%A2%E6%98%A0%E5%B0%84), `_` underline等符號
3. 不能用數字開頭
4. 可以用中文字
5. 大小寫英文視為不同

重點整理
變數a = 變數b，則兩者的ID會相同，原理是因為該動作只是在原本的Tag(Variable_01)，貼上第二個新的Tag(Variable_02)

### 2-4 運算子

#### 2-4-1 指定運算子
`=`號右邊的數值先計算，再回傳給左邊的Variant

#### 2-4-2 算術運算子
`+`, `-`, `*`, `/`(浮點除法), `//`(整數除法), `%`(相除後求餘數), `**`(次方)

遞增: 在算術運算子的右邊，加上等於，就是遞增(減)算法

Example:
```python
a = a + 1
a += 1 # 答案同上列 a + 1
```

#### 2-4-3 比較運算子
`<`, `<=`, `==`(等於), `!=`(不等於), `>=`, `>`

#### 2-4-4 邏輯運算子
`and`, `or`, `not`

#### 2-4-5 in, is 運算子

#### 2-4-6 位元運算
|符號|說明|
|-|-|
|`&`|位元且運算
|`\|`|位元或運算
|`^`|位元互斥或運算
|`~`|位元取相反
|`<<`|位元左移運算
|`>>`|位元右移運算

### 2-5 字串

String, 用`'string'`或`"string"`，都可以顯示字串

※不論是單引號或雙引號，都可以顯示包在裡面的引號

三引號，可以使用在多行文字(包括空白都會被列入範圍)

#### 2-5-1 字串運算子
* `+`: (合併str)
* `*N`: (重複N次字串)

#### 2-5-2 切割字串

|範例|動作|
|-|-|
`[5:]`|從5到結尾
`[:]`|從開始到結尾
`[-2:]`|從-2到結尾
`[:5]`|從開始到5
`[:-2]`|從開始到-3
`[7:9]`|從7~8
`[-4:-1]`|從-4~-2
`[5:-2]`|從5到-3
`[::-1]`|全部反轉
`[-1::-1]`|從-1到結尾，反轉
`[2:10:2]`|從2到9，間隔2

#### 2-5-3 串接多行
|符號|說明|
|-|-|
|`\`|一行(換行編寫)
|`\n`|換行
|`\t`|tab

### 2-6 彙整公式
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
### 3-1 Python的資料儲存容器

#### 3-1-1 儲存型態:
|型態|說明|
|-|-|
|tuple|依序儲存，可照順序取出，不可變
|list|依序儲存，可照順序取出，可變
|dict|Key:Value，無順序，可變
|set|無順序

---

## Chapter04
### 4-1 選擇結構

程式主要的3個結構:
1. 循環結構: 依序執行
2. 選擇結構: 條件測試
3. 重複結構: 重複執行

主要功能有:
- if
- elif
- else

※ 補充:
1. if可以簡化成這樣的公式寫法:
```python
x = 1
print('Test' if x == 1 else 'False')
# True回傳的值 if 條件 else False回傳的值
# ans: Test
```

---

## Chapter05

### 5-1 迴圈與生成式

主要功能:
- for
- while

#### 5-1-1 for while的基本組合應用

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

### 5-2 break, continue, else

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

### 5-3 for迴圈與資料儲存器
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

### 5-4 生成式 Comprehension

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
### 5-5 補充函數:

- python內建函數: `chr()` -> 返回一個整數值的ASCII字符
- python內建函數: `ord()` -> 返回一個值的十進制整數

---

## Chapter06

### 6-1 函式與遞迴

函式用於結構化程式，可以幫助多位程式設計師共同開發系統，
事先規劃好函式名稱與功能，再各自開發函式與整合所有程式，
最後達成系統所需功能。

### 6-2 函式的呼叫方法

1. `function_name(v01, v02, ...)` -> 無回傳值的呼叫方式
2. `variable_01 = function_name(v01, v02, ...)` -> 有回傳值的呼叫方式

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

### 6-3 位置引數(Positional arguments)

```python
# args裡面可以用','分隔輸入多個數值，會以tuple的方式呈現
def func_01(*args):
    print('位置引數為', args)
```

### 6-4 關鍵字引數(Keyword arguments)

```python
def func_02(**kwargs):
    print('關鍵字引數為', kwargs)
```
### 6-5 函式的說明文件

用三引號`""" text """`的方式，可以新增函式說明

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

### 6-6 函式視為物件 (object)

python中，函數視為object，加上`()`括號才會執行該程式。

### 6-7 函式lambda

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

### 6-8 函式產生器

```python
def irange(start: int, end: int, step=1):
    for i in range(start, end, step):
        yield i*i
x = irange(1, 10)

for i in x:
    print(i)
```

### 6-9 內部函式, closure函式

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

### 6-10 Decorator 裝飾器

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

### 6-11 遞迴 Recursion Function (遞迴函式)

```python
def recursive(a, b):

    if 條件判斷:
        return something
    else:
        return recursion_function
        # ex: recursive(參數a-1, 參數b+1)
```
## Chapter07

### 7-1 模組、套件與獨立程式

- 模組指的就是: 每一個python檔案
- 透過匯入其他python模組，就可以不斷地被其他程式再利用
- 單字: 變數、運算子等
- 句子: 多個變數、運算子、邏輯組合成一行程式
- 段落: 多行程式組合成函式
- 文章: 堆個函式組成模組

### 7-2 匯入模組的方式

```python
# 1
import sys
# 2
from sys import path
# 3
import sys as s
```

### 7-3 腳本程式

```python
if __name__ == '__main__:
    # doing something
```

---

## Chapter08

### 8-1 類別與例外

### 8-2 實例函數 (Instance class)
1. 隱藏參數: 在變數命名時，最前方加上兩個底線
```python
class A:
    def __init__(self, number):
        self.__number = number
```
2. 特殊函數__eq__的各式用法:
   |Function()|說明|
   |-|-|
   |\_\_eq__(self, other)|self == other
   |\_\_ne__(self, other)|self != other
   |\_\_gt__(self, other)|self > other
   |\_\_ge__(self, other)|self >= other
   |\_\_lt__(self, other)|self < other
   |\_\_le__(self, other)|self <= other
3. 範例

    ```python
    class Animal():
        # __init__表示宣告類別時，會自動執行的函式
        def __init__(self, name): # 第一個參數預設是self，後面可以放其他參數
            self.name = name
    a = Animal('動物')
    print(a.name) # 動物
    ```

### 8-3 繼承

- 原有的類別，被稱為:
  
    1. 基礎類別: base class
    2. 雙親類別: parent class
- 新的類別，被稱為:
  
    1. 衍生類別: derived class
    2. 子類別: child class

使用derived class來定義類別間的繼承關係，
衍生類別就繼承了基礎類別，在衍生類別使用***super().基礎類別的函數***，可以呼叫基礎類別的函式來幫忙。

```python
class Animal():
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__('小狗'+name) # Super()繼承name的屬性
a = Animal('動物')
b = Dog('小白')
print(a.name) # 動物
print(b.name) # 小狗小白
```

### 8-4 覆寫函式

衍生類別可以覆蓋(改寫)基礎類別中的相同名稱函數。

```python
class Animal():
    
    def __init__(self, name): # 不要把sound放入init屬性內
        self.name = name
    
    def sound(self):
        pass

class Dog(Animal):
    
    def __init__(self, name):
        super().__init__('小狗: ' + name)
    
    def sound(self): # 覆寫sound函式
        return '汪汪叫'

def main():
    
    d = Dog('小白')
    print(d.name)
    print(d.sound())
    
if __name__ == '__main__':
    main()
```

---

### 8-5 類別方法 (classmethod)

1. 直接在class最外層建立變數
2. 在function上方先加入`classmethod`
3. 在function參數中，新增`cls`
4. 此方法的function內部，可以用`cls.varirable_name`，來使用class variable

### 8-6 靜態方法 (staticmethod)

直接在class內部的函式上方，加入`staticmethod`

---

### 8-7 Exception 例外

- try... except ...
  
  可以攔截例外，在try區塊中撰寫可能會發生錯誤的情況，
  若發生錯誤，則會到except區塊執行後續的處理

- raise: 用來引發錯誤
- 可以有多個except來設定每個錯誤要執行的程式
- except IndexError as id: -> 用as可以命名
- else: 如果沒有異常中斷，則會接續執行else
- finally: 不論如何最終一定會執行的程式

```python
import os

try:
    test_list = [1, 2, 3, 4, 5]

    index = int(input('輸入索引值: '))

    if index not in test_list:

        raise IndexError
    
    print(test_list[index])

except IndexError:
    print('索引值超出範圍')

except Exception:
    print('發生其他錯誤')

```

---

## Chapter09

### 9-1 進階字串處理

### 9-2 ASCII

- 是最早的電腦系統編碼
- 只包含大小寫字母、數字、英文標點符號、數學運算符號與控制符號等
- 共128個字
- 將二進位編碼的控制符號轉換成十進位，介於0~31，再加上127，共33個 (32 + 1)
  
※ 常用功能:

`import string`
|function|用途|
|-|-|
|ascii_letters|大小寫字母
|ascii_lowercase|小寫
|ascii_uppercase|大小
|digits|十進位
|hexdigits|十六進位
|octdigits|八進位
|punctuation|標點符號
|printable|十進位數、全字母、標點、空白符號
|whitespace|空白字符

### 9-3 Unicode 編碼

Unicode可以分為4個十六進位，或8個十六進位表示

1. `\u` -> 4個十六進位: `\u6211` = '我'
2. `\U` -> 8個十六進位: `\U00006211` = '我'
3. `\N` -> 標準名稱: `\N{CJK UNIFIED IDEOGRAPH-6211}` = '我'

※ 常用功能:

`import unicodedata`

- `unicodedata.name('str')` -> 可以把字元轉換成標準名稱
- `unicodedata.lookup('str')` -> 可以把標準名稱轉換成字元

### 9-4 編碼 (encode)

- 將字串轉換成位元組(byte)，稱作編碼(encode)
- 將已編碼的位元組(byte)，還原成原來的字串，稱作解碼(decode)
- 目前最常用的是 UTF-8
  - 由Unicode編碼轉換
  - 每個字元由1到4個位元組表示
  - 位元組數量:
    - ASCII: 1
    - 拉丁、希臘、阿拉伯文: 2
    - 大部分中文: 3
    - 古義大利字母、日文假名補充、音樂符號: 4

### 9-5 解碼 (decode)

```python
    str.decode('utf8')
```

### 9-6 正規表示式 (regular expression)

使用正規表示式找尋特定字串是否存在，進行字串取代。

正規表示式常用於字串的分析與提取，python中的模組: `re`

```python
import re
```