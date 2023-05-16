# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。

s = int(input("输入一个不超过五位的数字"))
n = 0
# list1 = []
# while s != 0:
#     list1.append(s % 10)
#     s //= 10
#     n += 1
# print("它是一个", n, "位数")
# for i in list1:
#     print(i, end="\t")
# for i in range(n - 1, -1, -1):
#     print(list1[i], end="\t")

while s != 0:
    print(s % 10, end="\t")
    s //= 10
    n += 1
print("它是一个", n, "位数")