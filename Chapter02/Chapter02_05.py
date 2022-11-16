"""
str.split() ->切割字串
str.join(串列) -> 要串接的串列
str.replace(原始字串, 替代字串) -> 替代字串
str.find(要找的字串) -> 回傳找的字串位置，False == -1
str.startswith(要找的字串) -> 檢查字串是否以要找的字串開頭
str.endswith(要找的字串) -> 檢查字串是否以要找的字串結尾
str.count(要找的字串) -> 計算要找的字串出現次數
str.center(數值) -> 保留數值長度，置中字串 (rjust:置右，ljust:置左)
en_str.capitalize() -> 句首大寫
en_str.title() -> 每個單字字首大寫
en_str.swapcase() -> 大小寫互換
en_str.upper(), en_str.lower() -> 全大寫，全小寫
str.zill(width) -> 將字串左側補零(參照width)
str.strip(chars) -> 移除字串左右兩側的字元(chars)
"""

def main():
    
    # 用"，"來切割字串，回傳list
    s = '春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'
    s = s.split('，')
    print(s, type(s))
    
    # 使用join，串接起list
    list_01 = ['春眠不覺曉','處處聞啼鳥','夜來風雨聲','花落知多少。']
    s2 = '，'.join(list_01)
    print(s2)
    
    # 使用replace，取代字串
    list_01 = '春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'
    s3 = list_01.replace('眠', '秋')
    print(s3)
    
    # 使用find查找字串位置，rfind(從右邊開始找)
    list_01 = '明天要去宜蘭玩三天兩夜'
    print(list_01.find('宜蘭'))
    print(list_01.rfind('要'))
    print(list_01.find('台北'))
    
    # 使用startswith檢查字串是否以要找的字串開頭
    a = '超市現在有很多特價商品'
    print(a.startswith('超市'))
    print(a.startswith('現在'))
    
    # 使用endswith檢查字串是否以要找的字串結尾
    a = '台灣的高山茶很好喝'
    print(a.endswith('好喝'))
    
    # 使用count計算要找的字串之出現次數
    a = 'Pen Pineapple Apple Pen'
    print(a.count('Pen'))
    
    # center保留函式中數值長度，並置中文字 (rjust:置右, ljust:置左)
    a = 'Ben'
    print(a.center(20))
    print(a.ljust(20))
    print(a.rjust(20))
    
    # capitalize將英文字串的字首轉成大寫
    a = 'please advise the shipment.'
    print(a.capitalize())
    
    # title將每個單字字首轉成大寫
    a = 'please advise the shipment.'
    print(a.title())
    
    # swapcase將大小寫互換
    a = 'Please advise the Shipment.'
    print(a.swapcase())
    
    # upper, lower, 全部大、小寫
    a = 'Admin'
    print(a.lower(), a.upper())
    
    # str.zill(width) 將字串左側補零
    a = '456'
    print(a.zfill(6))
    
    # str.strip(chars) 移除字串左右兩側的字元(chars)，預設空白字元
    # lstrip(chars), rstrip(chars) 同用法
    a = ' Hello, Mary.   '
    b = a.strip()
    print(len(a), b, len(b))

def app_2_5_1():
    
    top = int(input('請輸入上衣數量: '))
    pants = int(input('請輸入褲子數量: '))
    undershirt = int(input('請輸入背心數量: '))
    amount = top*300 + pants*350 + undershirt*400
    print(f'總金額: {amount}元')

def app_2_5_5():
    
    a = input('請輸入字串: ')
    print(a == a[::-1])
    
def app_2_6():
    
    a = 'Keep something for a rainy day'
    b = a.split()
    c = a.title()
    print(f'{b}\n{c}')

if __name__ == '__main__':
    # main()
    app_2_6()