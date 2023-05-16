# 题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
#
# 程序分析：999999 / 13 = 76923。

x = int(input("请输入一个奇数"))
num = 0
x1 = 0
while True:
    x1 = x1 * 10 + 9
    num += 1
    if x1 % x == 0:
        break
print("9的个数：", num)
print(x1)
print(x1 // x)