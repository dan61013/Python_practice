import re

def main():
    
    s = '滿兩千打九折'
    
    ans01 = re.match('滿兩', s)
    # ans01 = re.match('九折', s) # 這個是False
    
    ans02 = re.search('兩千', s)
    
    if ans02:
        print(ans02.group())
    
    else:
        print(s)

if __name__ == '__main__':
    main()