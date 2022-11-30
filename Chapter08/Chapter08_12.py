# 例外 try except

def main():
    
    try:
        
        num = int(input('請輸入密碼: '))
        
    except EOFError:
        print('輸入EOF')
        
    except ValueError as ve:
        print(f'發生ValueError錯誤{ve}')
    
    except Exception as e:
        
        print(f'發生其他錯誤{e}')
    
    else:
        print(f'輸入的純數字密碼為: {num}')

if __name__ == '__main__':
    main()