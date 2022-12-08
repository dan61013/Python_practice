# 參考文章: 30天python雜談
# https://ithelp.ithome.com.tw/users/20107274/ironman/1578

def main():
    # python不需要先宣告type，是動態變數Dynamic type
    # 靜態變數要先宣告type, Static type
    a = 1
    b = a
    print(f'a={a}: id:{id(a)}, b={b}: id:{id(b)}, int 1: id:{id(1)}') # a, b, 1都是同一個記憶體位置
    # 代表變數是取得1這個整數的記憶體位置，call by reference
    
    # 舉例數值變化
    c = 1
    print(f'c id: {id(c)}') # 位置指向1的記憶體位置 by reference
    c += 1
    print(f'c += 1 id: {id(c)}') # 位置指向2的記憶體位置 by reference
    
    # 舉例list變化(dict同樣)
    # mutalbe
    b = ["Dan"]
    print(f'b id: {id(b)}') # 位置指向b這個list的位置
    b.append("Ben")
    print(f'b id: {id(b)}') # 所以即使新增值加入list，也不會改變id
    
if __name__ == "__main__":
    main()