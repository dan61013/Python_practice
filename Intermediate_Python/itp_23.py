# https://eastlakeside.gitbook.io/interpy-zh/exception
# exception 異常, try, except, raise, finally

def simply_sample():
    try:
        file = open('test.txt', 'rb')
    # 方式1: 將全部的Error放入同一個tuple內
    except (IOError, EOFError) as e:
        print("An IOError occured. {}.".format(e.args[-1]))
        
def test_01():
    # 處理多個異常的對應方式
    try:
        file = open('test.txt', 'rb')
    except EOFError as e:
        print("An EOF error occured.")
        raise e
    except IOError as e:
        print("An IO Error occured.")
        raise e

def test_02():
    # Exception: 所有錯誤類型
    try:
        file = open('test.txt', 'rb')
    except Exception:
        raise

def test_03():
    # finally: 無論如何都會執行
    try:
        file = open('test.txt', 'rb')
    except IOError as e:
        print("An IOError occured. {}".format(e.args[-1]))
    finally:
        print("This would be printed whether or not an exception occured!")

def main():
    # simply_sample()
    # test_01()
    # test_02()
    test_03()

if __name__ == "__main__":
    main()