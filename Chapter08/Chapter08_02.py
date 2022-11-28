# super的用法
# 參考文章: https://zhuanlan.zhihu.com/p/470778845

class PersonA():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def name_01(self, name):
        print("The name of PersonA is {}".format(name))
        
    def age_01(self, age):
        print("The age of PersonA is {}".format(age))

class PersonB(PersonA):
    
    # child class 繼承 parent class時，用super().__init__方式
    def __init__(self, name: str, age: int, sex: str):
        super().__init__(name, age)
        self.sex = sex
    
    def info(self, name, age):
        # info繼承parent的name_01 and age_01 function，並帶入自己的參數執行
        self.name_01(name)
        self.age_01(age)
    
    # def sex(self, sex):
    #     print("sex of PersonB is {}".format(sex))
    
    def sex_print(self):
        print("sex of PersonB is {}".format(self.sex))

def main():
    
    a = PersonB('Dan', 27, 'Man')
    print(a.name)
    print(a.age)
    print(a.info('LiSA', 30))
    print(a.sex)
    print(a.sex_print())

if __name__ == '__main__':
    main()