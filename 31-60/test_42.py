# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。
import math

again = True
while again:
    x = int(input("输入一个数字"))
    x = math.pow(x, 2)
    if x < 50:
        again = False
    else:
        again = True
        print(x)
