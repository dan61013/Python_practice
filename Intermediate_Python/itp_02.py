""" Debugging
https://eastlakeside.gitbook.io/interpy-zh/debugging
cmd: py -m pdb your_file_name.py
也可以import pdb，並在指定的line加入: pdb.set_trace()
c: 繼續執行
a: print當前函數列表
s: 單步進入
n: 單步跳過
w: 顯示當前程式碼的上下文訊息
"""
import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"

if __name__ == "__main__":
    print(make_bread())