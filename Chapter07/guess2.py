from guess import figure_guess

def run():
    
    computer = figure_guess()
    
    myself = input('輸入剪刀石頭布: ')
    print(f'電腦出: {computer}')
    
    if myself == "剪刀":
        if computer == "剪刀":
            print('平手')
        elif computer == "石頭":
            print('電腦獲勝')
        else:
            print('玩家獲勝')
    
    elif myself == "石頭":
        if computer == "石頭":
            print('平手')
        elif computer == "布":
            print('電腦獲勝')
        else:
            print('玩家獲勝')
    
    elif myself == "布":
        if computer == "布":
            print('平手')
        elif computer == "剪刀":
            print('電腦獲勝')
        else:
            print('玩家獲勝')

if __name__ == '__main__':
    
    for i in range(10):
        run()
    
    else:
        print('我不是獨立執行的python程式')