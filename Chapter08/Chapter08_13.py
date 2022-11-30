# 例外類別
# try ... except ... else ... finally

# 在class中的參數新增Exception (繼承系統例外類別)
class PasswordException(Exception):
    
    def __init__(self, pwd, len) -> None:
        super().__init__(self)
        self.pwd = pwd
        self.len = len
    
try:
    
    pwd = input('請輸入密碼，至少8個字元: ')
    if len(pwd) < 8:
        raise PasswordException(pwd, len(pwd))
except EOFError:
    print('輸入EOF')
except PasswordException as pex:
    print(f"密碼:{pex.pwd}\n長度為{pex.len}，密碼長度不足")
else:
    print(f'輸入密碼為: {pwd}')
# finally:
#     print('請妥善保管密碼')