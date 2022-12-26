# https://eastlakeside.gitbook.io/interpy-zh/coroutines
# 延伸閱讀: http://www.dabeaz.com/coroutines/Coroutines.pdf
# 協程
# Python中的協程與生成式很相似

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def grep(pattern):
    print("Searching for {}".format(pattern))
    while True:
        line = (yield)
        if pattern in line:
            print(line)

def main():
    # 生成式回顧
    # for i in fib():
        # print(i)
    search = grep('coroutine')
    next(search)
    search.send('I love you')
    search.send("Don't you love me?")
    search.send("I love coroutine instead!")
    search.close()
    # search.send('This is coroutine.') # Error

if __name__ == "__main__":
    main()