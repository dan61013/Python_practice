# https://eastlakeside.gitbook.io/interpy-zh/enumerate
# Enumerate, 枚舉，是內建函數，允許我們遍歷數據並自動記數

def sample_01():
    my_list = ['Dan', 'Ken', 'Ben', 'Amy']
    for c, value in enumerate(my_list, 1):
        print(c, value)
        
    # 建立包含索引的元組列表
    counter_list = list(enumerate(my_list, 1))
    print(counter_list, type(counter_list))

def main():
    
    # output -> 1 Dan, 2 Ken ...
    sample_01()

if __name__ == "__main__":
    main()