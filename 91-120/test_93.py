# 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
with open("file/test_1.txt") as f:
    a = f.read()
with open("file/test_2.txt") as f:
    b = f.read()
with open("file/test_3.txt", "w") as f:
    print(a+b)
    # 754123
    l = list(a + b)
    # ['7', '5', '4', '1', '2', '3']
    print(l)
    l.sort()
    s = " "
    s = s.join(l)
    f.write(s)
