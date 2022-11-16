"""
set, 使用set() 或 {}，可以建立set，會自動把重複的元素刪除
set() -> 只能使用一個參數，可以是 str, tuple, list, dict
"""

def main():
    
    # set()基本用法
    a1 = {1, 2, 3, 4}
    a2 = set((1, 2, 'a'))
    a3 = set(['a', 'a', 'p'])
    a4 = set({'a':0, 'b':1}) # dict只會取出key
    a5 = set(('string'))
    print(a1, a2, a3, a4, a5)
    
    # 聯集 | -> 雙方的元素合併
    a = set((1, 3, 5))
    b = set((3, 9, 11))
    print(a|b)
    
    # 交集 & -> 雙方都有的元素
    a = set((1, 3, 5))
    b = set((3, 9, 11))
    print(a&b)
    
    # 差集 - -> 存在於前方set, 但不存在於後方set
    a = set((1, 3, 5))
    b = set((3, 9, 11))
    print(a-b)
    
    # 互斥 ^ -> 去除存在於雙方的元素
    a = set((1, 3, 5))
    b = set((3, 9, 11))
    print(a^b)
    
    # 集合比較
    # 子集合, 真子集合, 超集合, 真超集合
    a = set('item')
    b = set('items')
    print(a<=b, a<b, a>=b, a>b)
    
def app_3_5_3():
    
    # 找出一段文字內的所有字(不重複)
    a = '空山不見人，但聞人語響。返景入深林，復照青苔上。'
    a = set(a)
    a.remove('，')
    a.remove('。')
    print(set(a))

def app_3_5_4():
    
    # 取出星期、月份
    week = ['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    month = ['','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
        'Octorber', 'November', 'December']
    dict01 = {'Week':week, 'Month':month}
    
    print(dict01['Month'][9], dict01['Week'][7])

def practice_01():
    
    # 輸入英文句子，去除空白或句點，回傳list
    sentence = input('請輸入英文句子: ').strip('.').strip()
    sentence = sentence.split(' ')
    print(sentence[::-1])

def practice_02():
    
    all_student = set(['Dan', 'Mindy', 'Irene', 'Fion', 'Amber', 'Helan'])
    
    english_pass = set(['Mindy', 'Irene', 'Fion', 'Amber', 'Helan'])
    
    math_pass = set(['Dan', 'Irene', 'Fion'])
    
    print(f'英文數學都及格: {english_pass&math_pass}\n數學不及格: {all_student-math_pass}\n\
英文及格(數學不及格): {english_pass&(all_student-math_pass)}')
    
def practice_03():
    
    # 製作email通訊錄
    
    directory = {}
    
    for _ in range(0, 3):
        name = str(input('請輸入名字: '))
        email = str(input('請輸入email: '))
        directory[name] = email
    
    find_name = str(input('請輸入要搜尋的名字: '))
    print(directory[find_name])

if __name__ == '__main__':
    # main()
    # app_3_5_3()
    # app_3_5_4()
    # practice_01()
    practice_03()