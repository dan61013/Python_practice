import re, string, unicodedata

def ch9_ex1(txt: str = "\u7a0b"):
    
    unicode_txt = unicodedata.name(txt)
    
    utf8 = unicodedata.lookup(unicode_txt)
    
    en = utf8.encode(encoding='utf8')

    print(f"{utf8}\n{unicode_txt}\n{en}")
    

def ch9_ex2():
    
    s = "123 ab 123.456 1d2.df -456"

    ans = re.findall("-?\d+\.?\d+", s)
    
    print(ans)

def ch9_ex3():
    
    s = "The best fish swim near the bottom."
    
    ans = re.findall("[A-Za-z]+", s)
    print(ans)
    
if __name__ == "__main__":
    ch9_ex3()