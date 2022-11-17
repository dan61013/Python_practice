"""
if 用法
"""

def main():
    pass

def app_4_1_1():
    
    """單向選擇結構"""
    score = int(input('請輸入分數: '))

    if score >= 60:
        print('很好，繼續保持！')
        
def app_4_2_1():
    
    """雙向選擇結構\n滿額折價"""
    total_price = int(input('滿2000打9折\n請輸入購買金額: '))
    
    print(f'折價後: {total_price if total_price < 2000 else int(total_price*0.9)}元')

def app_4_2_2():
    
    """判斷奇偶數"""
    num = int(input('請輸入一個整數: '))
    print(f'{num}是{"奇數" if num%2 != 0 else "偶數"}')

def app_4_2_3():
    
    """判斷可構三角形"""
    a, b, c = int(input('請輸入三角形a邊長度: ')),  int(input('請輸入三角形b邊長度: ')), \
        int(input('請輸入三角形c邊長度: '))
    print('可構三角形' if (a<b+c) and (a+b>c) and (b<a+c) else '無法構成三角形' )


if __name__ == '__main__':
    main()
    app_4_2_3()