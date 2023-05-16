# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
import math

x = int(input("输入一个整数："))
s = int(math.sqrt(x))
print(s)
for i in range(1, s + 1):
    if x % i == 0:
        print("不是素数")
        break
    if i == s:
        print("是素数")
