"""
break, continue, else
"""
import math

def main():
    
    # for 讀取tuple
    t = tuple('Tuple')
    for i in t:
        print(i)
    
    for i in range(0, len(t)):
        print(t[i])
        
    # for 讀取list
    shopping_list = ['牛奶', '礦泉水', '餅乾']
    
    for i in range(0, len(shopping_list)):
        print(shopping_list[i])
    
    # enumerate(list, 編號起始值)
    # for i, name -> i = 編號, name = shopping_list元素
    for i, name in enumerate(shopping_list, 1):
        print(i, name)

def ch5_5_4():
    
    for i in range(1, 6):
        print(i)
        
        if i == 3:
            print('next: while')
            break
    
    i = 1
    
    while i < 6:
        print(i)
        
        if i == 3:
            print('next: for + else')
            break
        
        i += 1
    
    for i in range(1, 6):
        print(i)
        
        if i == 6:
            break
        
    else:
        print('for迴圈正常結束')

def prime():
    """回傳數值是質數or非質數"""
    num = int(input('輸入一個整數: '))
    
    j = 2
    
    while j < math.sqrt(num):
        if num % j == 0:
            print("{}不是質數".format(num))
            break
        j += 1
        
    else:
        print('{}是質數'.format(num))

def ch5_4_1():
    """Login系統"""
    
    while True:
        account = input('請輸入帳號: ')
        password = input('請輸入密碼: ')
        
        if account == 'abc' and password == '123456':
            print('登入成功')
            break
        
        else:
            print('帳號密碼輸入錯誤，請重試')
            
def ch5_5_3():
    
    bboy_name = {'bboy01':'Kuma',
                 'bboy02':'Sprite',
                 'bboy03':'Kior',
                 'bboy04':'Kill'
                 }
    
    for key, value in bboy_name.items():
        print('{}選手是{}'.format(key, value))
    
    for key in bboy_name.keys():
        print(key, bboy_name[key])
        
    for value in bboy_name.values():
        print(value)

if __name__ == '__main__':
    # main()
    # ch5_4_1()
    ch5_5_3()