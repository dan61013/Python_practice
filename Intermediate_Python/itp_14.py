# https://eastlakeside.gitbook.io/interpy-zh/global_return
# Global, Return

# return方法
def add(value1, value2):
    return value1 + value2

# Global方法
def add_02(value1, value2):
    global ans
    ans = value1 + value2
    
# global實現多個return值
def profile():
    global name
    global age
    name = 'Dan'
    age = 27

def profile_02():
    name = 'Dan'
    age = 27
    return name, age

def main():
    result = add(3, 5)
    print(result) # 8
    
    add_02(3, 5)
    # 從函式外也能夠使用該變數
    print(ans) # 8
    
    # global方式
    profile()
    print(name)
    print(age)
    
    # 使用tuple方式
    profile_data = profile_02()
    print(profile_data[0])
    print(profile_data[1])

if __name__ == "__main__":
    main()