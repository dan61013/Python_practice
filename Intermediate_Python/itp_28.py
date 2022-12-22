# https://eastlakeside.gitbook.io/interpy-zh/c_extensions/ctypes
# C擴展
# 20221222 未完成: 因為要使用32位元的Python才能執行CDLL
# https://eastlakeside.gitbook.io/interpy-zh/c_extensions/python_c_api
# Python C API 未完成

from ctypes import *

# load the shared object file
adder = CDLL("./Intermediate_Python/adder.so") # Error

# Find sum of itegers
res_int = adder.add_int(4,5)
print(f"Sum of 4 and 5 = {str(res_int)}")