"""
Chapter05: 迴圈與生成式
"""

def main():
    for i in range(5):
        print(i)
    
    for i in range(100, 90, -3):
        print(i)

def app_ch5_5():
    for i in range(10):
        print('Hello')

def app_ch5_5_1_1():
    """產生ASCII碼, 65='A'"""
    start, end = int(input('輸入起始值: ')), int(input('輸入結束值: '))
    for i in range(start, end):
        print(chr(i))

def app_ch5_5_1_2():
    """sum加總"""
    start, end, itera = int(input('輸入起始值: ')), int(input('輸入結束值: ')), \
        int(input('遞增值: '))
    # sum加總由指定數值間隔產生的list
    # print(sum([i for i in range(start, end + 1, itera)]))
    # range產生的結果，type: range, range的type是type
    print(sum(range(start, end + 1, itera)))

if __name__ == '__main__':
    # main()
    # app_ch5_5()
    app_ch5_5_1_2()