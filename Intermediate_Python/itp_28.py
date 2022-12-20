# https://eastlakeside.gitbook.io/interpy-zh/c_extensions/ctypes
# C擴展

from ctypes import *

# load the shared object file
adder = CDLL("C:\\Users\\DanCai\\coding\\Python_practice\\Intermediate_Python\\adder.so") # Error

# Find sum of itegers
res_int = adder.add_int(4,5)
print(f"Sum of 4 and 5 = {str(res_int)}")