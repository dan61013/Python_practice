# Unicode編碼

import unicodedata

def main():
    
    # name default return Unicode \N{} (標準名稱)
    print(unicodedata.name('我'))
    
    word = '我'
    word_n = unicodedata.name(word)
    # 將Unicdoe標準名稱，轉換成Unicode標準字元
    word_unicode = unicodedata.lookup(word_n)
    
    word_01 = unicodedata.name('\u6211')
    word_02 = unicodedata.name('\U00006211')
    word_03 = unicodedata.name('\N{CJK UNIFIED IDEOGRAPH-6211}')
    
    print(word_unicode)
    print(word_01, word_02, word_03, sep='\t')

def unicode_name(name: str):
    
    value = unicodedata.name(name)
    
    print(f"Unicode字元: {name}\nUnicode標準名稱: {value}")

def unicode_lookup(name: str):
    
    unicode_u = unicodedata.lookup(name)
    
    print(f"Unicode字元: {unicode_u}\nUnicode標準名稱: {name}")
    
    

if __name__ == '__main__':
    # main()
    
    a = unicode_name('賣')
    b = unicode_lookup('CJK UNIFIED IDEOGRAPH-8CE3')