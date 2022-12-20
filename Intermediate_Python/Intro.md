# Intermediate Python
參考資料: [Intermediate Python 中譯](https://eastlakeside.gitbook.io/interpy-zh/)

* 目錄
    1. itp_01.py -> *args, **kwargs
    2. itp_02.py -> Debugging, 模組pdb
    3. itp_03.py -> Generator, 生成器，yield
    4. itp_04.py -> Generator, 生成器，yield
    5. itp_05.py -> map, lambda
    6. itp_06.py -> reduce, lambda
    7. itp_07.py -> set用法
    8. itp_08.py -> 三元運算子
    9. itp_09.py -> Decorator, 前置觀念
    10. itp_10.py -> Decorator, @
    11. itp_11.py -> Decorator應用
    12. itp_12.py -> 在函數中嵌入裝飾器
    13. itp_13.py -> 裝飾器類 Decorator class
    14. itp_14.py -> Global, Return
    15. itp_15.py -> mutable 對象變動
    16. itp_16.py -> slots魔法
    17. itp_17.py -> Collections.defaultdict and Counter
    18. itp_18.py -> Collections.deque and namedtuple
    19. itp_19.py -> Collections.namedtuple and enum.Enum
    20. itp_20.py -> enumerate
    21. itp_21.py -> type, id, dir and inspect.getmembers
    22. itp_21.py -> comprehension
    23. itp_22.py -> comprehension
    24. itp_23.py -> exception, try, else, finally
    25. itp_24.py -> class, 類變量與實例變量
    26. itp_25.py -> class, 屬性, init and getitem
    27. itp_26.py -> lambda (包含一個numpy的ithelp問題)
    28. 
## Decorator (函數中包含裝飾器)
* log檔是由itp_12.py，function: logit 產生
  
## 快速分享電腦中的Python檔案
```
py -m http.server
```

## 建立C的so共享檔案
```
// gcc c_filename.c -fPIC -shared -o so_filename.so
gcc add.c -fPIC -shared -o adder.so
```