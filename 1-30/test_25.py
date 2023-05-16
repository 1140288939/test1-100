# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
# 倒序输出 字符串
str1 = input("请输入多个字符")
len1 = 0


def output(i):
    if i == -1:
        return
    print(str1[i], end="")
    return output(i-1)


output(len(str1)-1)
