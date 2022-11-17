"""
多項選擇結構
"""

def main():
    pass

def app_4_3_1():
    
    """分數與評語"""
    score = int(input('請輸入成績: '))
    
    if score >= 80:
        print('非常好!')
    
    elif 60 <= score <80:
        print('不錯哦~')
    
    else:
        print('請加油~')

def app_4_3_2():
    
    """郵資計算"""
    weight = int(input('請輸入包裹重量: '))
    
    if weight <= 5:
        price = '50元'
    elif 5 < weight <= 10:
        price = '70元'
    elif 10 < weight <= 15:
        price = '90元'
    elif 15 < weight <= 20:
        price = '110元'
    else:
        price = '超過20KG，無法運送'    
    
    return print(price)

def app_4_3_3():
    
    """計算BMI"""
    height, weight = int(input('請輸入身高: ')), int(input('請輸入體重: '))
    bmi = weight / (height*2)
    
    if bmi < 18:
        grade = '體重過輕'
    
    elif 18 <= bmi < 24:
        grade = '體重正常'
    
    elif 24 <= bmi <27:
        grade = '體重過重'
    
    elif 27 <= bmi:
        grade = '體重肥胖'
    
    return print(f'BMI值: {bmi:.2f}, 肥胖分級: {grade}')

def app_4_4_1():
    
    """判斷數字是不是在tuple中"""
    a = (1, 2, 3, 4, 5)
    print(f'{"數字1在tuple a 中" if 1 in a else "數字1不在tuple a 中"}')
    
def app_4_4_2():
    
    """判斷串列list裡，是否包含某個元素"""
    list01 = list('apple')
    print(f"{'a在串列中' if 'a' in list01 else 'a不在串列中'}")

def app_4_4_3():
    
    """判斷元素是否在字典裡"""
    dict01 = {'Dan':'Cai', 'Mindy':'Yu'}
    print(f"'Dan的姓氏是'{dict01['Dan'] if 'Dan' in dict01 else '找不到Dan'}")

def app_4_4_4():
    
    """判斷元素是否在集合裡"""
    a = set('cat')
    if 'c' in a:
        print('c在集合a裡')
    
    else:
        print('c不在集合a裡')

if __name__ == '__main__':
    # main()
    app_4_4_4()