# https://eastlakeside.gitbook.io/interpy-zh/ternary_operators
# 三元運算子

"""
condition_is_True if condition else condition_uis_False
"""

def simply_sample():
    is_Man = True
    state = "Man" if is_Man else "not Man"
    print(state)
    
def tuple_if():
    """(if_test_is_false, if_test_is_true)[test]"""
    is_Man = True
    sex = ("Man", "Female")[is_Man] # 回傳0, tuple[0] = "Man"
    print("Dan is", sex)
    
def main():
    simply_sample()
    
if __name__ == "__main__":
    main()