# function encode
def main():
    
    # 7位元的ascii
    print('a'.encode(encoding='ascii'))
    
    # 轉換成可變長度的編碼，由1~4個位元組表一個unicode字元
    print('和'.encode(encoding='utf-8'))
    
    # \u and \U表示
    print('和'.encode(encoding='unicode-escape'))
    
    # ISO 8859-1 以ASCII為基礎，支援使用於歐洲的語言
    print('abc'.encode(encoding='latin-1'))

    a = '我'.encode(encoding='utf-8')
    b = a.decode('utf-8')
    print(a, b)
    print(b'\xe5\x92\x8c'.decode('utf-8'))

if __name__ == '__main__':
    main()