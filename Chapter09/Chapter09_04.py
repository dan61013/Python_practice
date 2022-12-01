# 正則表達式, import python內建模組 re
import re

def main():
    
    s = '滿兩千打九折'
    
    # re.match -> 找出字串中開頭是否符合match值
    ans01 = re.match('滿兩', s)
    # ans01 = re.match('九折', s) # 這個是False
    
    # re.search -> 找出字串中第一個符合的maych值
    ans02 = re.search('兩千', s)
    
    # re.findall -> 找出字串中全部符合match值
    ans03 = re.findall('打九', s)
    
    # re.split -> 使用pattern格式切割
    ans04 = re.split('九', s) # "九"會消失
    
    # re.sub -> 替代文字
    ans05 = re.sub('折', '十', s)
    
    # pattern格式可以用 '.' 代表任何字元，'.*'代表任何字元長度
    
    if ans05:
        # print(ans03.group())
        print(ans05)
    
    else:
        print(s)

def keyword():
    
    s = "a1 + b_2"
    
    # \d 匹配數字
    print(re.findall("\d", s))
    
    # \D 匹配非數字
    print(re.findall('\D', s))
    
    # \s 匹配空白字符
    print(re.findall('\s', s))
    
    # \S 匹配非空白字元
    print(re.findall("\S", s))
    
    # \w  匹配英數、底線、中文字元
    print(re.findall("\w", s))
    
    # \w  匹配非英數、底線、中文的標點符號
    print(re.findall("\W", s))
    
    # \b 匹配\w & \W的邊界，\b代表backspace
    # print(re.findall(r"\b", "abcd"))
    print(re.findall("\\b", "abcd"))
    
    # \B 匹配不在\w & \W的邊界
    print(re.findall("\B", "abcd"))

def regular_expression():
    
    s = "我要參加淡江盃比賽"
    
    # ^表示位置在開頭
    print(re.findall("^參加", s))
    print(re.findall("^淡江", s))
    
    # $表示位置在結尾
    print(re.findall("比賽$", s))
    
    # .配對除了Enter(\n)以外的字元
    print(re.findall(".江盃", s))
    print(re.findall("..江盃.", s))
    
    # x|y 配對或元素
    print(re.findall("淡|賽", s))
    
    # [xy] 可以配對多個字元
    print(re.findall('[淡盃]', s))
    
    # [^xy] 不是X且不是Y
    print(re.findall('[^賽參]', s))
    
    # x* 配對零or多個x，越多越好
    print(re.findall('[賽江]*', s))
    
    # x* 配對零or多個x，越少越好
    print(re.findall('[要]*?', s))
    
    # x+ 配對1or多個x，越多越好
    print(re.findall("[江我賽]+", s))
    
    # [0-9]+ 配對1個或多個0到9的數字，越多越好
    print(re.findall('[0-9]+', "123342 230239"))
    
    # [A-Za-z]+ 配對1個或多個英文字母，越多越好
    print(re.findall('[A-Za-z]+', "Time is money"))
    
    # x{a} 配對連續a個x
    print(re.findall("x{3}", "xyxzxxzraszx"))
    print(re.findall("x{2}", "xyxzxxzraszx"))
    
    # x{a,b}? 配對連續a到b個的x
    print(re.findall("x{2,3}?", "xxxxyyyyx"))
    
    # left(?=right) 配對左邊，如果後面有右邊
    print(re.findall('要(?=參加)', s))
    print(re.findall('要(?=比賽)', s)) # False
    
    # left(?!right) 配對左邊，如果後面沒有右邊
    print(re.findall("要(?!比賽)", s))
    print(re.findall("要(?!參加)", s))
    
    # (?<=left)right 配對右邊，如果前面有左邊
    print(re.findall("(?<=淡)江盃", s))
    print(re.findall("(?<=淡)比賽", s)) # False
    
    # (?<!left)right 配對右邊，如果前面沒有左邊
    print(re.findall("(?<!淡)江盃", s))
    print(re.findall("(?<!淡)比賽", s))
    
if __name__ == '__main__':
    # main()
    # keyword()
    regular_expression()