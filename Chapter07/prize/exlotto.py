import random

def lotto(n: int, m: int) -> list:
    """回傳樂透號碼:
n: 數字最大值
m: 取出m個數字"""

    # prize = list() # 與line9是一樣的意思
    prize = []
    nums = [i for i in range(1, n + 1)]
    
    for i in range(m):
        n = random.choice(nums)
        prize.append(n)
        nums.remove(n) # 從原本的清單中，移除隨機取出的數值
    return prize


if __name__ == '__main__':
    print(lotto(40, 5))