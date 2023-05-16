# 题目：练习函数调用。
# 程序分析：使用函数，输出三次 RUNOOB 字符串

def printR():
    print("Run")


def three():
    print("输出三次")
    for _ in range(3):
        printR()


if __name__ == "__main__":
    three()
