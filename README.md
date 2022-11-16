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
2. Input([prompt]) -> 顯示[prompt]，讓使用者輸入文字(default: String)

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

Example: a = a + 1 -> a += 1

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