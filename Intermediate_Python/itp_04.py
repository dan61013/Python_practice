# https://ithelp.ithome.com.tw/articles/10196328
# Generator

def my_range(n):
    """Simple example"""
    i = 0
    while i < n:
        print("我先在\"yield " + str(i) + "\"前睡了，等__next__來再叫我起床")
        yield i
        i += 1
        
if __name__ == "__main__":
    for i in my_range(5):
        print(i)