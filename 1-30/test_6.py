# 输出 9*9 乘法口诀表。

for i in range(1, 10):
    for j in range(1, i+1):
        # end 设置print最后的输出的符号；
        print("%d * %d = %d" % (j, i, i * j), end="\t")
    print()
