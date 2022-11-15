"""
str.split() ->切割字串
"""

def main():
    
    # 用，來切割字串，回傳list
    s = '春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'
    s = s.split('，')
    print(s, type(s))

if __name__ == '__main__':
    main()