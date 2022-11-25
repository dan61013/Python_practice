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

def ch6_ex2(m, n, ch):
    """印出m列n行的某個字元"""
    

def main():
    # n = int(input('輸入整數值: '))
    # ans = fac(n)
    # print('{}!為{}'.format(n, ans))

    m, n = int(input('輸入m值: ')), int(input('輸入n值: '))
    ans = gcd(m, n)
    print(f'{m}與{n}的最大公因數:{ans}',sep='')
    
if __name__ == '__main__':
    # main()
    pwd = input('請輸入密碼: ')
    sec = ch6_ex1(pwd)
    print(f'{pwd}為{sec}')