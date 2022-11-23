"""
while
"""
import random, math

def main():
    pass

def example_01():
    
    i = 3
    while i < 13:
        print(i)
        i += 3
        
def app_ch5_5_2_1():
    """計算N為多少時，其階乘會大於M等於"""
    m, i, n = int(input('請輸入M: ')), 1, 1
    
    while n < m:
        i += 1
        n *= i
    print(f"{i} 階乘為:{n} 大於 {m}")

def app_ch5_5_2_2():
    """猜數字"""
    x = None
    y = random.randint(1, 99)
    print('範圍:1~99')
    
    while x != y:
        x = int(input('猜整數: '))
        if x < y:
            print('猜大一點')
        elif x > y:
            print('猜小一點')
        else:
            print('猜中了~')

def app_ch5_5_2_3():
    """判斷質數"""
    num = int(input('請輸入一個整數: '))
    initial_num = 2
    p = True
    
    while initial_num < num:
        if num % initial_num == 0:
            p = False
            break
        initial_num += 1
    if p:
        print('{}是質數'.format(num))
    else:
        print('{}不是質數'.format(num))
        
def app_ch5_5_3_1():
    """99乘法表"""
    for i in range(1,10):
        for j in range(1, 10):
            # \t=tab, sep''取代空白字元, end''取代換行字元
            print(f"{i}*{j}={i*j}", '\t', sep='', end='')
        print() # 表示內層迴圈結束換行

def app_ch5_5_3_2():
    """列印出2~1000的所有質數"""
    for i in range(2, 1000):
        j = 2
        prime = True
        
        while j < math.sqrt(i):
            if i % j == 0:
                prime = False
                break
            j += 1
        if prime:
            print(i, '是質數')

if __name__ == '__main__':
    # main()
    # example_01()
    app_ch5_5_3_2()