# 两个变量值互换。

a = int(input("输入两个数"))
b = int(input("输入两个数"))

print("交换后输出")


def swap(a, b):
    # temp = b
    # b = a
    # a = temp
    a, b = b, a
    return a, b


a, b = swap(a, b)

print(a, b)
