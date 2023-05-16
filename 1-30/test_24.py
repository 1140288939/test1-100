# 利用递归方法求5!。

# 程序分析：递归公式：fn=fn_1*4!

def fn(x):
    if x == 1:
        return 1
    else:
        print(x)
        return x * fn(x - 1)


f = fn(5)
print(f)
