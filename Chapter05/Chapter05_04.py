"""
生成式(Comprehension)
產生器(Generator)
"""
import random

def main():
    pass

def ch5_5_6_1():
    
    a =[]
    
    for i in range(1, 6):
        a.append(i)
    print(a)
    
    # 生成式 Comprehension
    print([i for i in range(1, 6)])
    
    # 生成式 + if判斷
    print([i for i in range(1, 11) if i % 2 == 1])
    
    # 巢狀生成式
    print([i * j for i in range(1, 5) for j in range(1, 5)])
    
def nine_nine_table():
    
    print([f"{i}*{j}={i*j}" for i in range(1, 10) \
        for j in range(1, 10)])
    
def ch5_5_6_2():
    
    # 字典生成式
    word = 'AbCd'
    print({key : key for key in word})
    
    # Example
    # 列出字串中所有字母及出現次數
    word = 'Reformerz'
    word_count = {letter : word.count(letter) for letter in set(word)}
    print('每個單字的出現次數:')
    for w in word_count:
        print(f'{w} : {word_count[w]}')
        
    # 集合生成式
    word = 'Bboyworld'
    letters = {letter for letter in word}
    print(letters)

def ch5_5_6_4():
    
    # 產生器 Generator
    odd = (num for num in range(1, 10) if num % 2 == 1)
    print(odd)
    
    for num in odd:
        print(num)
    
    for num in odd:
        print(num) # 沒有值，因為產生器只能使用一次

def fibonacci():
    
    # 費氏定理
    num = int(input('輸入第幾項求費氏定理: '))
    a = 1
    b = 1
    print(1, a)
    for i in range(2, num + 1):
        a, b = b, a + b
        print(i, a)

def ch5_5_7_2():
    
    # 列出所有文字，並計算每個文字出現的次數
    s = """
君不見黃河之水天上來，奔流到海不復回。
君不見高堂明鏡悲白髮，朝如青絲暮成雪。
人生得意須盡歡，莫使金樽空對月。
天生我材必有用，千金散盡還復來。
烹羊宰牛且爲樂，會須一飲三百杯。
岑夫子，丹丘生。將進酒，杯莫停。
與君歌一曲，請君爲我傾耳聽。
鐘鼓饌玉不足貴，但願長醉不願醒。
古來聖賢皆寂寞，惟有飲者留其名。
陳王昔時宴平樂，斗酒十千恣歡謔。
主人何為言少錢？徑須沽取對君酌。
五花馬，千金裘。呼兒將出換美酒，與爾同銷萬古愁。"""

    dic = {w : s.count(w) for w in set(s) if w != '，' and w != '。' and w != '？'\
        and s.count(w) > 2 and w != '\n'}
    
    dic2 = {key:value for key, value in dic.items() if value == 3}
    
    print(dic)
    print(dic2)
    
def ch5_ex1():
    
    # 求平方和
    num = int(input('輸入項目值: '))
    
    sum = 0 # 給定一個變數當作起始值
    
    for i in range(1, num + 1):
        sum = sum + i*i # 每一次的加總值等於前一次的sum + 下一個i的平方
    print(sum)

def ch5_ex1_2():
    
    # 列出1~1000不被2 and 3整除的數值
    for i in range(1, 1001):
        if i % 2 != 0 and i % 3 != 0:
            print(i)

def ch5_5_7_3():
    
    sec1 = {chr(ord('a') + i):chr(ord('a') + i - 1) for i in range(26) if i % 2}
    sec2 = {chr(ord('a') + i):chr(ord('a') + i + 1) for i in range(26) if i % 2 == 0}
    
    sec1.update(sec2)
    
    print(sec1)
    
    s = 'bboy dan'
    print(s)
    
    ss = ''
    
    for c in s:
        if c != ' ':
            ss += sec1[c]
        else:
            ss += ' '
    print(ss)
    
    us = ''
    
    for c in ss:
        if c != ' ':
            us += sec1[c]
        else:
            us += ' '
    print(us)
    
def ch5_ex5():
    
    # 找出完全數
    # 設定範圍1~1000
    for i in range(1, 1001):
        
        # sum default = 0
        sum = 0
        
        for j in range(1, i):
            if i % j == 0:
                sum += j
                
        if sum == i:
            print('{}是完全數'.format(i))
            
def ch5_ex6():
    
    """擲骰子"""
    
    while True:
        dice = random.randint(1, 6)
        print(dice)
        
        if dice == 6:
            break

if __name__ == '__main__':
    
    # main()
    # ch5_5_7_3()
    ch5_ex6()
    # ch5_5_7_2()
    # nine_nine_table()
    # fibonacci()