# import guess # 一般import方式
# from guess import figure_guess # import module裡面的function
import guess as gs # import module as 簡稱
import sys # 使用sys.path方法，來查詢python匯入模組的路徑與順序

def main():
    computer = gs.figure_guess()
    print(computer)
    
    # 查詢python匯入模組的路徑與順序
    for path in sys.path:
        print(path)

if __name__ == '__main__':
    main()