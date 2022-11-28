def fac(num):
    """求n階層"""
    if num == 1:
        return 1
    
    else:
        return num*fac(num-1)

def gcd(m, n):
    """求最大公因數"""
    if m == 0:
        return n
    else:
        print(f'{m}與{n}的最大公因數相當於{n%m}與{m}的最大公因數')
        return gcd(n%m, m)

def ch6_ex1(password: str):
    if password.isdigit():
        if len(password) < 6:
            return '不安全的密碼'
        else:
            return '可能是安全的密碼'
    
    if password.isalpha():
        if len(password) < 6:
            return '不安全的密碼'
        else:
            return '可能是安全的密碼'
    elif len(password) < 6:
        return '不安全的密碼'
    elif len(password) < 10:
        return '安全的密碼'
    else:
        return '非常安全的密碼'

def ch6_ex2():
    """印出m列n行的某個字元"""
    m = int(input('請輸入列數: '))
    n = int(input('請輸入行數: '))
    ch = input('請輸入要重複的字元: ')
    for i in range(m):
        for j in range(n):
            print(ch, sep='', end='')
        print()

def ch6_ex3():
    
    score = [('Tina', 75, 90, 165), ('Tony', 80, 80, 160), ('Mary', 70, 85, 155), \
        ('John', 60, 70, 130)]
    
    # sorted score, 排序的key值: x等於 x 的第三個數值，reverse=Ture, 從大到小排列
    sorted_list = sorted(score, key=lambda x: x[3], reverse=True)
    print(sorted_list)
    
def ch6_ex4():
    
    n = int(input('輸入階層: '))
    
    result = 1
    
    for i in range(1, n + 1):
        
        result *= i
        yield result

def p_deco(func) -> str:
    def ptag(s: str) -> str:
        return '<p>' + func(s) + '</p>'
    return ptag

@p_deco
def phtml(s):
    
    return 'Hello,' + s

def ch6_ex6(num):
    """計算加總值"""
        
    if num == 1:
        return 1
    else:
        return num + ch6_ex6(num-1)

def main():
    # n = int(input('輸入整數值: '))
    # ans = fac(n)
    # print('{}!為{}'.format(n, ans))

    m, n = int(input('輸入m值: ')), int(input('輸入n值: '))
    ans = gcd(m, n)
    print(f'{m}與{n}的最大公因數:{ans}',sep='')
    
if __name__ == '__main__':
    # main()
    # pwd = input('請輸入密碼: ')
    # sec = ch6_ex1(pwd)
    # print(f'{pwd}為{sec}')
    n = int(input('輸入n值等於: '))
    ans = ch6_ex6(n)
    print('Answer: {}'.format(ans))
    # print(phtml('Dan'))
    # for i in ch6_ex4():
        # print(i)