# 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

n = int(input("输入一个整数"))


def call1(n):
    print(n)
    if n <= 0:
        return 0
    else:
        return 1/n + call1(n-2)


print(call1(n))
