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

if __name__ == "__main__":
    test_var_args('test', 'python', 'javascript', 'C++', 'R')
    test_kwargs(Name="Dan", Age=27)