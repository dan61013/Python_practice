"""
Chapter01: Python的輸入及輸出
"""

def main():
    # print(*objects)
    # 將objects顯示在螢幕上，字元間隔預設(sep)，使用一個空白鍵
    print('開始','練習','python') # 學習 python 的第一步
    
    # print(*objects, sep='\t', end='\n')，\t -> Tab鍵, \n -> 換行
    print('開始','練習','python', sep='\t', end= '\n')
    
    # input([prompt提示])
    # f'str {objects}'，在String前面加上f，可以用"{}"輸入變數及運算
    name = input('Input your name: ')
    print(f'Hello, {name}!')

def app_1_4():
    # 第一個Python程式
    name = input('請輸入你的名字: ')
    print(f'Hello, {name}')
    age = input('請輸入你的年齡: ')
    print(f'原來你{age}歲')
    height = input('請問你的身高是幾公分: ')
    print(f'身高為: {height}cm')

if __name__ == '__main__':
    main()
    app_1_4()