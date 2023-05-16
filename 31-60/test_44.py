# 题目：数字比较。

a = int(input("输入一个数"))
b = int(input("输入一个数"))

if a > b:
    print("%d 大于 %d" % (a, b))
elif a < b:
    print("%d 小于 %d" % (a, b))
else:
    print("%d 等于 %d" % (a, b))
