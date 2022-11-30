# string模組提供ASCII字碼
import string, random

def ch9_9_1_2():
    
    pwd_keyword_list = string.ascii_letters + string.digits

    pwd = ''
    
    for i in range(random.randint(8, 12)):
        pwd += random.choice(pwd_keyword_list)
    
    print(f"密碼產生: {pwd}\t長度: {len(pwd)}")

def main():
    
    # 大小寫字母，共52個
    a = string.ascii_letters
    
    # lower and upper
    b = string.ascii_lowercase
    c = string.ascii_uppercase
    
    # 數字
    d = string.digits # 十進位
    e = string.hexdigits # 十六進位
    f = string.octdigits # 八進位
    
    # 標點符號
    g = string.punctuation
    
    # 十進位數字、大小寫字母，標點與空白符號，共100個
    h = string.printable
    
    # 空白字元
    i = string.whitespace
    
    
    print(a, type(a)) # type: String
    print(a[10])
    
    print(b, type(b))
    print(c, type(c))

    print(d, e, f, sep='\n')
    
    print(g)
    
    print(h)
    
    print(i)
    
if __name__ == '__main__':
    # main()
    ch9_9_1_2()