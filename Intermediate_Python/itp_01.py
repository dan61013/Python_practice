# *args用法
def test_var_args(first_arg, *args):
    # 輸出first_arg (第一個參數)
    print("The first normal arg: {}".format(first_arg))
    
    for arg in args:
        print("Another arg through *args: {}".format(arg))

# **kwargs用法
def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        # 輸出key == value
        print("{} == {}".format(key, value))
        
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

def main():
    # 設定tuple包含3個object
    args = ("two", 1, 10)
    # 使用*args
    test_args_kwargs(*args)
    
    # 使用**kwargs
    kwargs = {"arg3":3, "arg2": 101, "arg1": "Test"}
    test_args_kwargs(**kwargs)

if __name__ == "__main__":
    test_var_args('test', 'python', 'javascript', 'C++', 'R')
    test_kwargs(Name="Dan", Age=27) # **kwargs用key=value的方式輸入
    main()