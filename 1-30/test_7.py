# 题目：暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。


import time

mydict = {"a": 1, "b": 2}
for k, v in dict.items(mydict):
    print(k, v)
    time.sleep(1)
